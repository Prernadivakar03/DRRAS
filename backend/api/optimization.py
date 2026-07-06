


from pulp import LpMaximize, LpProblem, LpVariable, lpSum
from api.models import DisasterCluster, ResourceData, OptimizedAllocation

def optimize_resource_allocation():
    # Step 1: Fetch Clustering Data
    clustered_disasters = DisasterCluster.objects.all()
    resource_data = ResourceData.objects.all()

    # Step 2: Group Data by Cluster Priority
    cluster_priority = {"High": 1, "Moderate": 2, "Low": 3}  # Lower number = higher priority
    clustered_disasters = sorted(clustered_disasters, key=lambda d: cluster_priority.get(d.cluster_label, 3))

    # Step 3: Create Optimization Problem
    problem = LpProblem("Resource_Allocation", LpMaximize)

    # Step 4: Define Variables
    allocation_vars = {
        (r.resource_id, d.disaster_id): LpVariable(f"alloc_{r.resource_id}_{d.disaster_id}", lowBound=0, cat="Continuous")
        for r in resource_data for d in clustered_disasters if r.disaster_id == d.disaster.id
    }

    # Step 5: Define Objective Function (Maximize total allocated resources)
    problem += lpSum(allocation_vars.values())

    # Step 6: Add Constraints
    for r in resource_data:
        problem += lpSum(allocation_vars[(r.resource_id, d.disaster.id)] for d in clustered_disasters if (r.resource_id, d.disaster.id) in allocation_vars) <= r.quantity  # Don't exceed available resources

    # Step 7: Solve the Optimization Problem
    problem.solve()

    # Step 8: Store Results in Database
    OptimizedAllocation.objects.all().delete()  # Clear previous allocations
    allocations = []
    for (resource_id, disaster_id), var in allocation_vars.items():
        if var.varValue > 0:
            disaster = DisasterCluster.objects.get(disaster_id=disaster_id)
            resource = ResourceData.objects.get(resource_id=resource_id)
            allocations.append(OptimizedAllocation(
                location=disaster.disaster.location,
                disaster_type=disaster.disaster.disaster_type,
                impact_level=disaster.cluster_label,
                cluster_label=disaster.cluster_label,
                resource_name=resource.resource_type,
                allocated_resources=var.varValue,
                source = disaster.source
            ))

    OptimizedAllocation.objects.bulk_create(allocations)
    
    return "Resource allocation completed successfully."
#impcode 

