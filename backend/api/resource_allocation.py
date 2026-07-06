
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserDisasterCluster, UserInput, ResourceData, OptimizedAllocation
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def allocate_resources_with_pulp(request):
    """
    Allocate multiple resource types to disaster clusters using PuLP.
    For each disaster, a minimum total resource requirement is set based on severity.
    The allocation minimises total usage while respecting per‑resource availability.
    If supply is insufficient, slack variables allow shortages (penalised) so a solution is always found.
    """
    disasters = UserDisasterCluster.objects.all()
    resources = ResourceData.objects.all()

    if not disasters.exists():
        return JsonResponse({"message": "No disasters found. No resources allocated."})

    if not resources.exists():
        return JsonResponse({"message": "No resources available."})

    logger.info("Available resources:")
    for res in resources:
        logger.info(f"  {res.resource_type}: {res.quantity}")

    # Build a dictionary of resource type -> available quantity
    resource_pool = {res.resource_type: res.quantity for res in resources}
    resource_types = list(resource_pool.keys())

    # Build disaster list with required minimum total allocation
    disaster_data = []
    for d in disasters:
        if d.cluster_label == "Severe Impact":
            required = 300
        elif d.cluster_label == "Moderate Impact":
            required = 50
        else:
            required = 0   # no minimum for other clusters
        # Link to UserInput for location and disaster_type
        user_input = UserInput.objects.filter(id=d.user_disaster_id).first()
        location = user_input.location if user_input else "Unknown Location"
        disaster_type = user_input.disaster_type if user_input else "Unknown Disaster"
        disaster_data.append({
            "id": d.id,
            "location": location,
            "disaster_type": disaster_type,
            "cluster_label": d.cluster_label,
            "required": required,
        })

    # ---- Build the LP problem ----
    prob = LpProblem("Resource_Allocation", LpMinimize)

    # Decision variables: amount of each resource type allocated to each disaster
    alloc_vars = {}
    for d in disaster_data:
        for r_type in resource_types:
            var_name = f"alloc_{d['id']}_{r_type.replace(' ', '_')}"
            alloc_vars[(d['id'], r_type)] = LpVariable(var_name, lowBound=0, cat="Continuous")

    # Slack variables for each disaster (shortage relative to required)
    slack_vars = {}
    for d in disaster_data:
        slack_vars[d['id']] = LpVariable(f"slack_{d['id']}", lowBound=0, cat="Continuous")

    # Objective: minimise total allocated resources + heavy penalty for shortages
    total_alloc = lpSum(alloc_vars.values())
    shortage_penalty = lpSum(1000 * slack_vars[d['id']] for d in disaster_data)  # high penalty
    prob += total_alloc + shortage_penalty

    # Constraints:
    # 1. For each disaster, sum of allocated resources + slack >= required
    for d in disaster_data:
        prob += (
            lpSum(alloc_vars[(d['id'], r_type)] for r_type in resource_types) + slack_vars[d['id']]
            >= d['required']
        )

    # 2. For each resource type, total allocated cannot exceed available quantity
    for r_type in resource_types:
        prob += (
            lpSum(alloc_vars[(d['id'], r_type)] for d in disaster_data)
            <= resource_pool[r_type]
        )

    # Solve
    prob.solve()
    status = LpStatus[prob.status]
    logger.info(f"Solver status: {status}")

    # Check if an optimal or feasible solution was found (status may be 'Optimal' or 'Feasible')
    # PuLP returns 'Optimal' if solved to optimality; 'Feasible' if a feasible solution exists.
    # With slack variables, we should always get a feasible solution unless the problem is unbounded.
    if status not in ['Optimal', 'Feasible']:
        return JsonResponse({
            "message": f"Resource allocation failed. Solver status: {status}",
            "allocations": []
        }, status=400)

    # ---- Save allocations to database ----
    allocations = []
    for d in disaster_data:
        for r_type in resource_types:
            allocated = value(alloc_vars[(d['id'], r_type)]) or 0.0
            if allocated > 0:  # only save if positive
                OptimizedAllocation.objects.create(
                    location=d['location'],
                    disaster_type=d['disaster_type'],
                    cluster_label=d['cluster_label'],
                    resource_name=r_type,
                    allocated_resources=allocated
                )
                allocations.append({
                    "disaster_id": d['id'],
                    "location": d['location'],
                    "disaster_type": d['disaster_type'],
                    "impact_level": d['cluster_label'],
                    "resource_type": r_type,
                    "allocated_resources": allocated
                })

    # Optionally log shortage information
    total_shortage = sum(value(slack_vars[d['id']]) or 0 for d in disaster_data)
    if total_shortage > 0:
        logger.warning(f"Total shortage across all disasters: {total_shortage}")

    return JsonResponse({
        "message": "Resource allocation completed successfully!",
        "allocations": allocations,
        "total_shortage": total_shortage
    })