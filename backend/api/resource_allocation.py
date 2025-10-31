

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import UserDisasterCluster, UserInput, ResourceData, OptimizedAllocation
# from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# @csrf_exempt
# def allocate_resources_with_pulp(request):
#     # Fetch disasters that need resource allocation
#     disasters_to_allocate = UserDisasterCluster.objects.all()
    
#     if not disasters_to_allocate.exists():
#         return JsonResponse({"message": "No disasters found. No resources allocated."})

#     # Fetch available resources
#     resources = ResourceData.objects.all()
#     if not resources.exists():
#         return JsonResponse({"message": "No resources available."})

#     # Create an optimization model
#     problem = LpProblem("Resource_Allocation", LpMinimize)

#     # Decision variables for resource allocation
#     allocation_vars = {
#         disaster.id: LpVariable(f"alloc_{disaster.id}", lowBound=0, cat="Continuous")  # Min 0 allocation
#         for disaster in disasters_to_allocate
#     }

#     # Objective function: Minimize total resource allocation
#     problem += lpSum(allocation_vars.values())

#     # Constraints: Allocate resources proportionally based on disaster severity
#     for disaster in disasters_to_allocate:
#         if disaster.cluster_label == "Severe Impact":
#             problem += allocation_vars[disaster.id] >= 500  # Minimum allocation for severe impact
#         elif disaster.cluster_label == "Moderate Impact":
#             problem += allocation_vars[disaster.id] >= 100  # Minimum allocation for moderate impact

#     # Constraint: Do not exceed total available resources
#     total_available = sum(res.quantity for res in resources)
#     problem += lpSum(allocation_vars.values()) <= total_available

#     # Solve the optimization problem
#     problem.solve()

#     allocations = []

#     for disaster in disasters_to_allocate:
#         allocated_amount = max(0, allocation_vars[disaster.id].varValue or 0)  # Ensure non-negative allocation

#         # Fetch disaster details from UserInput using user_disaster_id
#         matched_user_input = UserInput.objects.filter(id=disaster.user_disaster_id).first()

#         location = matched_user_input.location if matched_user_input else "Unknown Location"
#         disaster_type = matched_user_input.disaster_type if matched_user_input else "Unknown Disaster"

#         # Assign the first available resource (modify as needed)
#         resource = resources.first()
#         resource_type = resource.resource_type if resource else "General Resource"

#         # Store the allocated data in the database
#         OptimizedAllocation.objects.create(
#             location=location,  
#             disaster_type=disaster_type,  
#             cluster_label=disaster.cluster_label,  # ✅ Fixed attribute
#             resource_name=resource_type,
#             allocated_resources=allocated_amount
#         )

#         # Prepare response data
#         allocations.append({
#             "disaster_id": disaster.id,
#             "location": location,  
#             "disaster_type": disaster_type,  
#             "impact_level": disaster.cluster_label,  # ✅ Fixed attribute
#             "resource_type": resource_type,
#             "allocated_resources": allocated_amount
#         })

#     return JsonResponse({"message": "Resource allocation completed successfully!", "allocations": allocations})
#imp 
















































































































from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserDisasterCluster, UserInput, ResourceData, OptimizedAllocation
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, LpStatus

@csrf_exempt
def allocate_resources_with_pulp(request):
    disasters_to_allocate = UserDisasterCluster.objects.all()
    resources = ResourceData.objects.all()

    if not disasters_to_allocate.exists():
        return JsonResponse({"message": "No disasters found. No resources allocated."})

    if not resources.exists():
        return JsonResponse({"message": "No resources available."})

    print("Checking available resources in the database...")
    total_available = sum(res.quantity for res in resources)
    for res in resources:
        print(f"Resource: {res.resource_type}, Quantity: {res.quantity}")

    print("\nChecking disasters to allocate...")
    for disaster in disasters_to_allocate:
        print(f"Disaster ID: {disaster.id}, Severity: {disaster.cluster_label}")

    problem = LpProblem("Resource_Allocation", LpMinimize)
    
    allocation_vars = {
        disaster.id: LpVariable(f"alloc_{disaster.id}", lowBound=0, cat="Continuous")
        for disaster in disasters_to_allocate
    }

    problem += lpSum(allocation_vars.values())  # Minimize total allocation

    for disaster in disasters_to_allocate:
        if disaster.cluster_label == "Severe Impact":
            problem += allocation_vars[disaster.id] >= 300  # Adjusted threshold
        elif disaster.cluster_label == "Moderate Impact":
            problem += allocation_vars[disaster.id] >= 50

    problem += lpSum(allocation_vars.values()) <= total_available

    problem.solve()
    print("\nSolver Status:", LpStatus[problem.status])

    allocations = []
    for disaster in disasters_to_allocate:
        allocated_amount = max(0, value(allocation_vars[disaster.id]) or 0)
        print(f"Disaster {disaster.id}: Allocated {allocated_amount}")

        matched_user_input = UserInput.objects.filter(id=disaster.user_disaster_id).first()
        location = matched_user_input.location if matched_user_input else "Unknown Location"
        disaster_type = matched_user_input.disaster_type if matched_user_input else "Unknown Disaster"

        resource = resources.first()
        resource_type = resource.resource_type if resource else "General Resource"

        OptimizedAllocation.objects.create(
            location=location,
            disaster_type=disaster_type,
            cluster_label=disaster.cluster_label,
            resource_name=resource_type,
            allocated_resources=allocated_amount
        )

        allocations.append({
            "disaster_id": disaster.id,
            "location": location,
            "disaster_type": disaster_type,
            "impact_level": disaster.cluster_label,
            "resource_type": resource_type,
            "allocated_resources": allocated_amount
        })

    return JsonResponse({"message": "Resource allocation completed successfully!", "allocations": allocations})
