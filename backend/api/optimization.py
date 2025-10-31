# import pulp
# from django.db import transaction
# from .models import ResourceData, UserInput, OptimizedAllocation, DisasterCluster, DisasterData

# def optimize_resource_allocation():
#     try:
#         # 1️⃣ **Fetch Necessary Data**
#         clusters = list(DisasterCluster.objects.select_related("disaster").values("disaster_id", "cluster_label"))
#         resources = list(ResourceData.objects.values("resource_id", "disaster_id", "resource_type", "quantity", "location"))
#         disasters = {d["id"]: d for d in DisasterData.objects.values("id", "disaster_type", "impact_level")}

#         if not clusters or not resources:
#             return {"error": "No disaster clusters or resources found"}

#         # 2️⃣ **Sort Clusters by Impact** (Severe First → Moderate → Low)
#         impact_priority = {"Severe": 0, "Moderate": 1, "Low": 2}
#         sorted_clusters = sorted(clusters, key=lambda x: impact_priority.get(disasters.get(x["disaster_id"], {}).get("impact_level", "Low"), 2))

#         # 3️⃣ **Define Optimization Problem**
#         prob = pulp.LpProblem("Resource_Allocation", pulp.LpMaximize)
#         allocation_vars = {}

#         for cluster in sorted_clusters:
#             for resource in resources:
#                 if cluster["disaster_id"] == resource["disaster_id"]:  # Match disasters
#                     var_name = f"alloc_{cluster['disaster_id']}_{resource['resource_id']}"
#                     allocation_vars[(cluster["disaster_id"], resource["resource_id"])] = pulp.LpVariable(var_name, lowBound=0, cat="Integer")

#         # 4️⃣ **Objective Function: Maximize Allocation**
#         prob += pulp.lpSum(allocation_vars.values())

#         # 5️⃣ **Constraints: Don't Exceed Available Quantity**
#         for resource in resources:
#             prob += pulp.lpSum(allocation_vars[(c["disaster_id"], resource["resource_id"])] for c in sorted_clusters if (c["disaster_id"], resource["resource_id"]) in allocation_vars) <= resource["quantity"]

#         # 6️⃣ **Solve Optimization Problem**
#         prob.solve()

#         # 7️⃣ **Store Results in Database**
#         with transaction.atomic():
#             OptimizedAllocation.objects.all().delete()  # Clear old results
#             for (disaster_id, resource_id), var in allocation_vars.items():
#                 allocated = var.varValue
#                 if allocated > 0:
#                     resource_obj = next((r for r in resources if r["resource_id"] == resource_id), None)
#                     disaster_obj = disasters.get(disaster_id, {})

#                     if resource_obj:
#                         OptimizedAllocation.objects.create(
#                             location=resource_obj["location"],
#                             disaster_type=disaster_obj.get("disaster_type", "Unknown"),
#                             impact_level=disaster_obj.get("impact_level", "Low"),
#                             cluster_label=next((c["cluster_label"] for c in clusters if c["disaster_id"] == disaster_id), "N/A"),
#                             resource_name=resource_obj["resource_type"],
#                             allocated_resources=allocated,
#                         )

#         return {"message": "Optimization completed successfully", "allocated_resources": len(allocation_vars)}

#     except Exception as e:
#         return {"error": str(e)}

















































# import pulp
# from django.db import transaction
# from .models import ResourceData, UserInput, OptimizedAllocation, DisasterCluster, DisasterData

# def optimize_resource_allocation():
#     try:
#         # 1️⃣ **Fetch Data from Database**
#         clusters = list(DisasterCluster.objects.select_related("disaster").values("disaster_id", "cluster_label"))
#         resources = list(ResourceData.objects.values("resource_id", "disaster_id", "resource_type", "quantity", "location"))
#         disasters = {d["id"]: d for d in DisasterData.objects.values("id", "disaster_type", "impact_level")}

#         if not clusters or not resources:
#             return {"error": "No disaster clusters or resources found"}

#         # 2️⃣ **Sort Clusters by Impact** (Severe → Moderate → Low)
#         impact_priority = {"Severe": 3, "Moderate": 2, "Low": 1}
#         sorted_clusters = sorted(clusters, key=lambda x: impact_priority.get(disasters.get(x["disaster_id"], {}).get("impact_level", "Low"), 1), reverse=True)

#         # 3️⃣ **Define Linear Programming Problem**
#         prob = pulp.LpProblem("Resource_Allocation", pulp.LpMaximize)
#         allocation_vars = {}

#         # 4️⃣ **Decision Variables: Allocate resources to disasters**
#         for cluster in sorted_clusters:
#             for resource in resources:
#                 if cluster["disaster_id"] == resource["disaster_id"]:  # Match disasters
#                     var_name = f"alloc_{cluster['disaster_id']}_{resource['resource_id']}"
#                     allocation_vars[(cluster["disaster_id"], resource["resource_id"])] = pulp.LpVariable(var_name, lowBound=0, cat="Integer")

#         # 5️⃣ **Objective Function: Prioritize Severe Impact Clusters**
#         prob += pulp.lpSum(
#             impact_priority[disasters.get(c["disaster_id"], {}).get("impact_level", "Low")] * allocation_vars[(c["disaster_id"], r["resource_id"])]
#             for c in sorted_clusters for r in resources if (c["disaster_id"], r["resource_id"]) in allocation_vars
#         )

#         # 6️⃣ **Constraints**
#         # a) **Don't allocate more than available quantity**
#         for resource in resources:
#             prob += pulp.lpSum(
#                 allocation_vars[(c["disaster_id"], resource["resource_id"])]
#                 for c in sorted_clusters if (c["disaster_id"], resource["resource_id"]) in allocation_vars
#             ) <= resource["quantity"]

#         # b) **Ensure positive allocation values**
#         for (disaster_id, resource_id), var in allocation_vars.items():
#             prob += var >= 0

#         # 7️⃣ **Solve Optimization Problem**
#         prob.solve()

#         # 8️⃣ **Store Results in Database**
#         with transaction.atomic():
#             OptimizedAllocation.objects.all().delete()  # Clear old results
#             for (disaster_id, resource_id), var in allocation_vars.items():
#                 allocated = var.varValue
#                 if allocated > 0:
#                     resource_obj = next((r for r in resources if r["resource_id"] == resource_id), None)
#                     disaster_obj = disasters.get(disaster_id, {})

#                     if resource_obj:
#                         OptimizedAllocation.objects.create(
#                             location=resource_obj["location"],
#                             disaster_type=disaster_obj.get("disaster_type", "Unknown"),
#                             impact_level=disaster_obj.get("impact_level", "Low"),
#                             cluster_label=next((c["cluster_label"] for c in clusters if c["disaster_id"] == disaster_id), "N/A"),
#                             resource_name=resource_obj["resource_type"],
#                             allocated_resources=allocated,
#                         )

#         return {"message": "Optimization completed successfully", "allocated_resources": len(allocation_vars)}

#     except Exception as e:
#         return {"error": str(e)}
















































# from ortools.linear_solver import pywraplp
# from django.db import transaction
# from .models import DisasterCluster, ResourceData, OptimizedAllocation

# def optimize_resource_allocation():
#     """
#     Allocates resources optimally using OR-Tools Linear Programming.
#     Prioritizes high-impact disaster clusters first.
#     """
#     try:
#         # 1️⃣ **Fetch Clusters & Resources**
#         clusters = list(DisasterCluster.objects.select_related("disaster").values(
#             "id", "disaster_id", "cluster", "disaster__location", "disaster__disaster_type"
#         ))
#         resources = list(ResourceData.objects.values(
#             "id", "disaster_id", "resource_type", "quantity", "location"
#         ))

#         if not clusters or not resources:
#             return {"error": "No clusters or resources available for optimization."}

#         # 2️⃣ **Sort Clusters by Severity (Severe → Moderate → Low)**
#         clusters.sort(key=lambda x: x["cluster"])

#         # 3️⃣ **Define Linear Programming Model**
#         solver = pywraplp.Solver.CreateSolver("SCIP")  # SCIP solver (efficient for large problems)
#         if not solver:
#             return {"error": "Solver initialization failed."}

#         # 4️⃣ **Create Allocation Variables**
#         allocation_vars = {}
#         for cluster in clusters:
#             for resource in resources:
#                 if cluster["disaster_id"] == resource["disaster_id"]:  # Match resources to disasters
#                     var_name = f"alloc_{cluster['id']}_{resource['id']}"
#                     allocation_vars[(cluster["id"], resource["id"])] = solver.IntVar(0, resource["quantity"], var_name)

#         # 5️⃣ **Objective Function: Maximize Resource Distribution**
#         solver.Maximize(
#             solver.Sum(allocation_vars[(c["id"], r["id"])] for c in clusters for r in resources if (c["id"], r["id"]) in allocation_vars)
#         )

#         # 6️⃣ **Constraints:**
#         # a) Ensure total allocation does not exceed resource quantity
#         for resource in resources:
#             solver.Add(
#                 solver.Sum(allocation_vars[(c["id"], resource["id"])] for c in clusters if (c["id"], resource["id"]) in allocation_vars)
#                 <= resource["quantity"]
#             )

#         # b) Set priority allocation limits (e.g., Severe gets more)
#         allocation_limits = {0: 2000, 1: 1000, 2: 500}  # Limits for each cluster type
#         for cluster in clusters:
#             solver.Add(
#                 solver.Sum(allocation_vars[(cluster["id"], r["id"])] for r in resources if (cluster["id"], r["id"]) in allocation_vars)
#                 <= allocation_limits.get(cluster["cluster"], 500)
#             )

#         # 7️⃣ **Solve Optimization Problem**
#         status = solver.Solve()
#         if status != pywraplp.Solver.OPTIMAL:
#             return {"error": "No optimal solution found."}

#         # 8️⃣ **Store Optimized Results in Database**
#         with transaction.atomic():
#             OptimizedAllocation.objects.all().delete()  # Clear old results
#             for (cluster_id, resource_id), var in allocation_vars.items():
#                 allocated = var.solution_value()
#                 if allocated > 0:
#                     cluster_obj = next(c for c in clusters if c["id"] == cluster_id)
#                     resource_obj = next(r for r in resources if r["id"] == resource_id)

#                     OptimizedAllocation.objects.create(
#                         location=resource_obj["location"],
#                         disaster_type=cluster_obj["disaster__disaster_type"],
#                         impact_level=3 - cluster_obj["cluster"],  # Convert 0=Severe, 1=Moderate, 2=Low
#                         cluster_label=f"Cluster {cluster_obj['cluster']}",
#                         resource_name=resource_obj["resource_type"],
#                         allocated_resources=allocated,
#                     )

#         return {"message": "Optimization completed successfully", "allocated_resources": len(allocation_vars)}

#     except Exception as e:
#         return {"error": str(e)}

# def optimize_resource_allocation():
#     print("🚀 Running Resource Allocation Optimization...")  # Debug print




























































































# from ortools.linear_solver import pywraplp
# from django.db import transaction
# from .models import DisasterCluster, ResourceData, OptimizedAllocation

# def optimize_resource_allocation():
#     """
#     Allocates resources optimally using OR-Tools Linear Programming.
#     Prioritizes high-impact disaster clusters first.
#     """
#     try:
#         print("🚀 Running Resource Allocation Optimization...")  

#         # 1️⃣ **Fetch Clusters & Resources from Database**
#         clusters = list(DisasterCluster.objects.select_related("disaster").values(
#             "id", "disaster_id", "cluster", "disaster__location", "disaster__disaster_type"
#         ))
#         resources = list(ResourceData.objects.values(
#             "id", "disaster_id", "resource_type", "quantity", "location"
#         ))

#         if not clusters:
#             return {"error": "❌ No disaster clusters found in the database."}
#         if not resources:
#             return {"error": "❌ No available resources for allocation."}

#         print(f"✅ Loaded {len(clusters)} clusters and {len(resources)} resources.")  

#         # 2️⃣ **Sort Clusters by Severity (Severe → Moderate → Low)**
#         impact_priority = {0: "Severe Impact", 1: "Moderate Impact", 2: "Low Impact"}
#         clusters.sort(key=lambda x: x["cluster"])  

#         # 3️⃣ **Match Resources to Clusters**
#         cluster_dict = {c["disaster_id"]: c for c in clusters}
#         filtered_resources = [r for r in resources if r["disaster_id"] in cluster_dict]

#         if not filtered_resources:
#             return {"error": "❌ No matching resources found for disaster clusters."}

#         print(f"✅ Matched {len(filtered_resources)} resources to disaster clusters.")  

#         # 4️⃣ **Initialize OR-Tools Solver**
#         solver = pywraplp.Solver.CreateSolver("SCIP")  
#         if not solver:
#             return {"error": "❌ Solver initialization failed."}

#         # 5️⃣ **Define Allocation Variables**
#         allocation_vars = {}
#         for cluster in clusters:
#             for resource in filtered_resources:
#                 if cluster["disaster_id"] == resource["disaster_id"]:  
#                     var_name = f"alloc_{cluster['id']}_{resource['id']}"
#                     allocation_vars[(cluster["id"], resource["id"])] = solver.IntVar(0, resource["quantity"], var_name)

#         print(f"✅ Created {len(allocation_vars)} allocation variables.")  

#         if not allocation_vars:
#             return {"error": "❌ No valid allocation variables found."}

#         # 6️⃣ **Define Objective Function: Maximize Resource Distribution**
#         solver.Maximize(
#             solver.Sum(allocation_vars[(c["id"], r["id"])] for c in clusters for r in filtered_resources if (c["id"], r["id"]) in allocation_vars)
#         )

#         # 7️⃣ **Constraints:**
#         # a) Resource Allocation Constraints
#         for resource in filtered_resources:
#             solver.Add(
#                 solver.Sum(allocation_vars[(c["id"], resource["id"])] for c in clusters if (c["id"], resource["id"]) in allocation_vars)
#                 <= resource["quantity"]
#             )

#         # b) Priority-Based Allocation (Severe gets more)
#         allocation_limits = {0: 2000, 1: 1000, 2: 500}  
#         for cluster in clusters:
#             solver.Add(
#                 solver.Sum(allocation_vars[(cluster["id"], r["id"])] for r in filtered_resources if (cluster["id"], r["id"]) in allocation_vars)
#                 <= allocation_limits.get(cluster["cluster"], 500)
#             )

#         print("✅ Constraints set. Solving the problem...")  

#         # 8️⃣ **Solve Optimization Problem**
#         status = solver.Solve()
#         if status != pywraplp.Solver.OPTIMAL:
#             return {"error": "❌ No optimal solution found."}

#         print("✅ Solution Found! Storing results...")  

#         # 9️⃣ **Store Optimized Results in Database**
#         with transaction.atomic():
#             OptimizedAllocation.objects.all().delete()  
#             allocations_saved = 0
#             optimized_allocations = []

#             for (cluster_id, resource_id), var in allocation_vars.items():
#                 allocated = var.solution_value()
#                 if allocated > 0:
#                     cluster_obj = next(c for c in clusters if c["id"] == cluster_id)
#                     resource_obj = next(r for r in filtered_resources if r["id"] == resource_id)

#                     # ✅ Store in Database
#                     OptimizedAllocation.objects.create(
#                         location=resource_obj["location"],
#                         disaster_type=cluster_obj["disaster__disaster_type"],
#                         impact_level=impact_priority[cluster_obj["cluster"]],  
#                         cluster_label=f"Cluster {cluster_obj['cluster']}",
#                         resource_name=resource_obj["resource_type"],
#                         allocated_resources=allocated,
#                     )

#                     # ✅ Store in response
#                     optimized_allocations.append({
#                         "location": resource_obj["location"],
#                         "disaster_type": cluster_obj["disaster__disaster_type"],
#                         "impact_level": impact_priority[cluster_obj["cluster"]],
#                         "cluster_no": cluster_obj["cluster"],
#                         "resource_name": resource_obj["resource_type"],
#                         "allocated_quantity": allocated
#                     })

#                     allocations_saved += 1

#         print(f"✅ Successfully stored {allocations_saved} optimized allocations.")  

#         # 🔥 **Return the structured API response**
#         return {
#             "message": "✅ Optimization completed successfully",
#             "allocated_resources": allocations_saved,
#             "allocations": optimized_allocations
#         }

#     except Exception as e:
#         return {"error": str(e)}




















































# from ortools.linear_solver import pywraplp
# from django.db import transaction
# from .models import DisasterCluster, ResourceData, OptimizedAllocation

# BATCH_SIZE = 500  # Process 500 disasters at a time

# def optimize_resource_allocation():
#     solver = pywraplp.Solver.CreateSolver('SCIP')
#     if not solver:
#         print("Solver not available!")
#         return

#     # ✅ Fetch disaster clusters (prioritizing high-severity)
#     disaster_batches = DisasterCluster.objects.select_related('disaster').order_by('cluster').iterator(chunk_size=BATCH_SIZE)

#     # ✅ Fetch unique resource types
#     resource_types = list(ResourceData.objects.values_list('resource_type', flat=True).distinct())

#     if not resource_types:
#         print("No resource data available!")
#         return

#     for disaster_batch in disaster_batches:
#         disaster_list = list(disaster_batch)  # Convert iterator batch to list
#         allocation_vars = {}

#         # ✅ Define decision variables (allocation of each resource type)
#         for disaster in disaster_list:
#             for resource_type in resource_types:
#                 allocation_vars[(disaster.id, resource_type)] = solver.NumVar(0, solver.infinity(), f'alloc_{disaster.id}_{resource_type}')

#         # ✅ Objective Function: Maximize total allocated resources
#         solver.Maximize(solver.Sum(allocation_vars.values()))

#         # ✅ Constraint: Ensure allocation does not exceed required quantity
#         for disaster in disaster_list:
#             solver.Add(
#                 solver.Sum(allocation_vars[(disaster.id, resource_type)] for resource_type in resource_types)
#                 <= disaster.disaster.people_affected * 2  # Required quantity based on affected people
#             )

#         # ✅ Solve optimization for this batch
#         status = solver.Solve()
#         if status == pywraplp.Solver.OPTIMAL:
#             print(f"Optimal solution found for batch of {len(disaster_list)} disasters!")

#             # ✅ Store allocations in batch
#             allocation_objects = []
#             for (disaster_id, resource_type), var in allocation_vars.items():
#                 if var.solution_value() > 0:
#                     disaster = DisasterCluster.objects.get(id=disaster_id)
#                     allocation_objects.append(
#                         OptimizedAllocation(
#                             location=disaster.disaster.location,
#                             disaster_type=disaster.disaster.disaster_type,
#                             impact_level=disaster.disaster.impact_level,
#                             cluster_label=f'Cluster {disaster.cluster}',
#                             resource_name=resource_type,
#                             allocated_resources=var.solution_value()
#                         )
#                     )

#             # ✅ Insert allocations in batches
#             with transaction.atomic():
#                 OptimizedAllocation.objects.bulk_create(allocation_objects)

#         else:
#             print(f"No optimal solution found for batch of {len(disaster_list)} disasters.")

#     print("Batch-wise resource allocation completed successfully!")





































# from ortools.linear_solver import pywraplp
# from django.db import transaction
# from .models import DisasterCluster, ResourceData, OptimizedAllocation

# BATCH_SIZE = 500  # Process 500 disasters at a time

# def optimize_resource_allocation():
#     solver = pywraplp.Solver.CreateSolver('SCIP')
#     if not solver:
#         print("Solver not available!")
#         return

#     # ✅ Fetch disaster clusters in batches
#     disaster_clusters = DisasterCluster.objects.select_related('disaster').order_by('cluster')
    
#     # ✅ Fetch unique resource types
#     resource_types = list(ResourceData.objects.values_list('resource_type', flat=True).distinct())

#     if not resource_types:
#         print("No resource data available!")
#         return

#     # ✅ Process disasters in batches
#     cluster_list = list(disaster_clusters)  # Convert to list for proper batching
#     for i in range(0, len(cluster_list), BATCH_SIZE):
#         disaster_batch = cluster_list[i:i + BATCH_SIZE]
#         allocation_vars = {}

#         # ✅ Define decision variables (allocation of each resource type)
#         for disaster in disaster_batch:
#             for resource_type in resource_types:
#                 allocation_vars[(disaster.id, resource_type)] = solver.NumVar(
#                     0, solver.infinity(), f'alloc_{disaster.id}_{resource_type}'
#                 )

#         # ✅ Objective Function: Maximize total allocated resources
#         solver.Maximize(solver.Sum(allocation_vars.values()))

#         # ✅ Constraint: Ensure allocation does not exceed required quantity
#         for disaster in disaster_batch:
#             solver.Add(
#                 solver.Sum(allocation_vars[(disaster.id, resource_type)] for resource_type in resource_types)
#                 <= disaster.disaster.people_affected * 2  # Required quantity based on affected people
#             )

#         # ✅ Solve optimization for this batch
#         status = solver.Solve()
#         if status == pywraplp.Solver.OPTIMAL:
#             print(f"✅ Optimal solution found for batch of {len(disaster_batch)} disasters!")

#             # ✅ Store allocations in batch
#             allocation_objects = [
#                 OptimizedAllocation(
#                     location=disaster.disaster.location,
#                     disaster_type=disaster.disaster.disaster_type,
#                     impact_level=disaster.disaster.impact_level,
#                     cluster_label=f'Cluster {disaster.cluster}',
#                     resource_name=resource_type,
#                     allocated_resources=var.solution_value()
#                 )
#                 for (disaster_id, resource_type), var in allocation_vars.items()
#                 if var.solution_value() > 0
#                 for disaster in disaster_batch if disaster.id == disaster_id  # Ensure correct disaster match
#             ]

#             # ✅ Insert allocations in batches
#             with transaction.atomic():
#                 OptimizedAllocation.objects.bulk_create(allocation_objects)

#         else:
#             print(f"⚠️ No optimal solution found for batch of {len(disaster_batch)} disasters.")

#     print("🎯 Batch-wise resource allocation completed successfully!")


















































































































# import pandas as pd
# import numpy as np
# from pulp import LpVariable, LpProblem, LpMinimize, lpSum, LpStatus
# from django.db.models import Sum, Avg, F
# from api.models import DisasterCluster, ResourceData

# # ================================
# # 1️⃣ Load Data from Django Database
# # ================================

# # ✅ Fetch disaster clusters
# cluster_queryset = DisasterCluster.objects.values("disaster_id", "cluster")
# cluster_df = pd.DataFrame(list(cluster_queryset))

# # ✅ Fetch resource allocation data
# resource_queryset = ResourceData.objects.values("resource_id", "disaster_id", "resource_type", "quantity", "cost_usd")
# resource_df = pd.DataFrame(list(resource_queryset))

# # ================================
# # 2️⃣ Ensure Data Consistency (Convert IDs to Integer)
# # ================================
# cluster_df["disaster_id"] = cluster_df["disaster_id"].astype(int)
# resource_df["disaster_id"] = resource_df["disaster_id"].astype(str).str.extract(r'(\d+)').astype(float).astype("Int64")

# # ================================
# # 3️⃣ Merge Cluster & Resource Data
# # ================================
# merged_df = cluster_df.merge(resource_df, on="disaster_id", how="inner")

# # ================================
# # 4️⃣ Ensure Unique "Resource ID" with Aggregation
# # ================================
# resource_df = resource_df.groupby("resource_id", as_index=False).agg({
#     "quantity": "sum",
#     "resource_type": "first",
#     "cost_usd": "mean"
# })

# # ✅ Create dictionaries for quick lookup
# cost_dict = resource_df.set_index("resource_id")["cost_usd"].to_dict()
# quantity_dict = resource_df.set_index("resource_id")["quantity"].to_dict()
# type_dict = resource_df.set_index("resource_id")["resource_type"].to_dict()

# # ================================
# # 5️⃣ Define Resource Allocation Variables
# # ================================
# allocation = {
#     (row["cluster"], row["resource_id"]): LpVariable(f"alloc_{row['cluster']}_{row['resource_id']}", 
#                                                      0, quantity_dict[row["resource_id"]]) 
#     for _, row in merged_df.iterrows()
# }

# # ================================
# # 6️⃣ Create Optimization Model
# # ================================
# model = LpProblem("Resource_Allocation", LpMinimize)

# # 🎯 **Objective Function: Minimize Total Cost**
# model += lpSum(allocation[key] * cost_dict[key[1]] for key in allocation), "Total_Cost"

# # ================================
# # 7️⃣ Add Constraints (Ensure Allocation)
# # ================================

# # **Demand Constraint**: Each cluster gets a minimum required amount
# demand_per_cluster = merged_df.groupby("cluster")["quantity"].sum().to_dict()

# for cluster_id, demand in demand_per_cluster.items():
#     model += lpSum(allocation[(cluster_id, res_id)] for res_id in quantity_dict.keys() if (cluster_id, res_id) in allocation) >= demand * 0.3, f"Demand_Cluster_{cluster_id}"

# # **Supply Constraint**: Do not exceed available supply
# for res_id in quantity_dict.keys():
#     model += lpSum(allocation[(cl, res_id)] for cl in cluster_df["cluster"].unique() if (cl, res_id) in allocation) <= quantity_dict[res_id], f"Supply_Resource_{res_id}"

# # ================================
# # 8️⃣ Solve the Model
# # ================================
# model.solve()

# # ================================
# # 9️⃣ Save Results to Database
# # ================================
# from api.models import OptimizedAllocation

# # ✅ Clear previous allocations (optional)
# OptimizedAllocation.objects.all().delete()

# allocation_entries = []
# for k, v in allocation.items():
#     allocated_qty = v.varValue if v.varValue is not None else 0
#     if allocated_qty > 0:  # Only save non-zero allocations
#         allocation_entries.append(OptimizedAllocation(
#             location="Unknown",  # You can update this with actual location data
#             disaster_id=merged_df[merged_df["cluster"] == k[0]]["disaster_id"].iloc[0],
#             impact_level="Medium",  # Placeholder, update as needed
#             cluster_id=k[0],
#             resource_name=type_dict[k[1]],
#             allocated_resources=allocated_qty
#         ))

# # ✅ Bulk insert for efficiency
# OptimizedAllocation.objects.bulk_create(allocation_entries)

# # ================================
# # 🔥 Print Final Optimization Results
# # ================================
# print(f"Optimization Status: {LpStatus[model.status]}\n")

# for entry in allocation_entries:
#     print(f"Cluster {entry.cluster_id} - Resource {entry.resource_name}: Allocated {entry.allocated_resources}")



















































































































# import pandas as pd
# import numpy as np
# from pulp import LpVariable, LpProblem, LpMinimize, lpSum, LpStatus
# from django.db.models import Sum, F
# from api.models import DisasterCluster, ResourceData, OptimizedAllocation

# # ================================
# # 1️⃣ Load Data from Django Database
# # ================================

# # ✅ Fetch disaster clusters
# cluster_queryset = DisasterCluster.objects.values("disaster_id", "cluster", "cluster_label")
# cluster_df = pd.DataFrame(list(cluster_queryset))

# # ✅ Fetch resource allocation data
# resource_queryset = ResourceData.objects.values("resource_id", "disaster_id", "resource_type", "quantity", "cost_usd")
# resource_df = pd.DataFrame(list(resource_queryset))

# # ================================
# # 2️⃣ Ensure Data Consistency
# # ================================
# if not cluster_df.empty:
#     cluster_df["disaster_id"] = cluster_df["disaster_id"].astype(str).str.extract(r'(\d+)').astype(float).astype(int)

# if not resource_df.empty:
#     resource_df["disaster_id"] = resource_df["disaster_id"].astype(str).str.extract(r'(\d+)').astype(float).astype(int)

# # ✅ Merge Cluster & Resource Data
# merged_df = cluster_df.merge(resource_df, on="disaster_id", how="inner")

# # ================================
# # 3️⃣ Ensure Unique "Resource ID" with Aggregation
# # ================================
# if not resource_df.empty:
#     resource_df = resource_df.groupby("resource_id", as_index=False).agg({
#         "quantity": "sum",
#         "resource_type": "first",
#         "cost_usd": "mean"
#     })

# # ✅ Create lookup dictionaries
# cost_dict = resource_df.set_index("resource_id")["cost_usd"].to_dict() if not resource_df.empty else {}
# quantity_dict = resource_df.set_index("resource_id")["quantity"].to_dict() if not resource_df.empty else {}
# type_dict = resource_df.set_index("resource_id")["resource_type"].to_dict() if not resource_df.empty else {}

# # ================================
# # 4️⃣ Define Resource Allocation Variables
# # ================================
# allocation = {}
# for _, row in merged_df.iterrows():
#     key = (row["cluster"], row["resource_id"])
#     allocation[key] = LpVariable(f"alloc_{row['cluster']}_{row['resource_id']}", 0, quantity_dict.get(row["resource_id"], 0))

# # ================================
# # 5️⃣ Create Optimization Model
# # ================================
# model = LpProblem("Resource_Allocation", LpMinimize)

# # 🎯 **Objective Function: Minimize Total Cost**
# model += lpSum(allocation[key] * cost_dict.get(key[1], 0) for key in allocation), "Total_Cost"

# # ================================
# # 6️⃣ Add Constraints (Ensure Allocation)
# # ================================

# # **Demand Constraint**: Each cluster gets at least 30% of total demand
# demand_per_cluster = merged_df.groupby("cluster")["quantity"].sum().to_dict()

# for cluster_id, demand in demand_per_cluster.items():
#     model += lpSum(allocation.get((cluster_id, res_id), 0) for res_id in quantity_dict.keys()) >= demand * 0.3, f"Demand_Cluster_{cluster_id}"

# # **Supply Constraint**: Do not exceed available supply
# for res_id in quantity_dict.keys():
#     model += lpSum(allocation.get((cl, res_id), 0) for cl in cluster_df["cluster"].unique()) <= quantity_dict[res_id], f"Supply_Resource_{res_id}"

# # ================================
# # 7️⃣ Solve the Model
# # ================================
# model.solve()

# # ================================
# # 8️⃣ Save Results to Database
# # ================================

# # ✅ Clear previous allocations (optional)
# OptimizedAllocation.objects.all().delete()

# allocation_entries = []
# for (cluster_id, res_id), v in allocation.items():
#     allocated_qty = v.varValue if v.varValue is not None else 0
#     if allocated_qty > 0:  # Save only non-zero allocations
#         cluster_instance = cluster_df[cluster_df["cluster"] == cluster_id].iloc[0] if not cluster_df.empty else {}

#         allocation_entries.append(OptimizedAllocation(
#             location="Unknown",  # No location data in DisasterCluster, update as needed
#             disaster_type="Unknown",  # No disaster type data in this approach
#             impact_level="Medium",  # Placeholder, update as needed
#             cluster_label=cluster_instance.get("cluster_label", "Unknown"),  
#             resource_name=type_dict.get(res_id, "Unknown"),  
#             allocated_resources=allocated_qty
#         ))

# # ✅ Bulk insert for efficiency
# if allocation_entries:
#     OptimizedAllocation.objects.bulk_create(allocation_entries)

# # ================================
# # 🔥 Print Final Optimization Results
# # ================================
# print(f"Optimization Status: {LpStatus[model.status]}\n")

# for entry in allocation_entries:
#     print(f"Cluster {entry.cluster_label} - Resource {entry.resource_name}: Allocated {entry.allocated_resources}")






























































































































# import pandas as pd
# import numpy as np
# from pulp import LpVariable, LpProblem, LpMinimize, lpSum, LpStatus
# from django.db.models import Sum
# from api.models import DisasterCluster, ResourceData, OptimizedAllocation

# def optimize_resource_allocation():
#     print("Starting optimization...")

#     # ✅ Fetch Data from Database
#     cluster_queryset = DisasterCluster.objects.values("disaster_id", "id", "cluster_label")
#     resource_queryset = ResourceData.objects.values("resource_id", "disaster_id", "resource_type", "quantity", "cost_usd")
    
#     cluster_df = pd.DataFrame(list(cluster_queryset))
#     resource_df = pd.DataFrame(list(resource_queryset))

#     # ✅ Standardize column names for consistency
#     cluster_df.columns = cluster_df.columns.str.strip().str.lower().str.replace(" ", "_")
#     resource_df.columns = resource_df.columns.str.strip().str.lower().str.replace(" ", "_")

#     # ✅ Ensure Proper Data Types
#     cluster_df["disaster_id"] = pd.to_numeric(cluster_df["disaster_id"], errors="coerce").fillna(0).astype(int)
#     resource_df["disaster_id"] = pd.to_numeric(resource_df["disaster_id"], errors="coerce").fillna(0).astype(int)

#     # ✅ Merge Cluster & Resource Data (Left Join to Keep All Clusters)
#     merged_df = cluster_df.merge(resource_df, on="disaster_id", how="left").fillna(0)

#     # ✅ Aggregate Resource Data
#     if not resource_df.empty:
#         resource_df = resource_df.groupby("resource_id", as_index=False).agg({
#             "quantity": "sum",
#             "resource_type": "first",
#             "cost_usd": "mean"
#         })

#     # ✅ Create Lookup Dictionaries
#     cost_dict = resource_df.set_index("resource_id")["cost_usd"].to_dict() if not resource_df.empty else {}
#     quantity_dict = resource_df.set_index("resource_id")["quantity"].to_dict() if not resource_df.empty else {}
#     type_dict = resource_df.set_index("resource_id")["resource_type"].to_dict() if not resource_df.empty else {}

#     # ✅ Define Optimization Variables
#     allocation = {
#         (row["id"], row["resource_id"]): LpVariable(f"alloc_{row['id']}_{row['resource_id']}", 0, quantity_dict.get(row["resource_id"], 0))
#         for _, row in merged_df.iterrows()
#     }

#     # ✅ Create Optimization Model
#     model = LpProblem("Resource_Allocation", LpMinimize)
#     model += lpSum(allocation[key] * cost_dict.get(key[1], 0) for key in allocation), "Total_Cost"

#     # ✅ Demand Constraints (At least 30% of required resources)
#     demand_per_cluster = merged_df.groupby("id")["quantity"].sum().to_dict()
#     for cluster_id, demand in demand_per_cluster.items():
#         model += lpSum(allocation.get((cluster_id, res_id), 0) for res_id in quantity_dict.keys()) >= demand * 0.3, f"Demand_Cluster_{cluster_id}"

#     # ✅ Supply Constraints (Do not exceed available resources)
#     for res_id in quantity_dict.keys():
#         model += lpSum(allocation.get((cl, res_id), 0) for cl in cluster_df["id"].unique()) <= quantity_dict[res_id], f"Supply_Resource_{res_id}"

#     # ✅ Solve the Model
#     model.solve()

#     # ✅ Save Results to Database
#     OptimizedAllocation.objects.all().delete()
#     allocation_entries = []

#     for (cluster_id, res_id), v in allocation.items():
#         allocated_qty = v.varValue if v.varValue is not None else 0
#         if allocated_qty > 0:
#             cluster_instance = cluster_df[cluster_df["id"] == cluster_id].to_dict(orient="records")
#             cluster_instance = cluster_instance[0] if cluster_instance else {"cluster_label": "Unknown"}

#             allocation_entries.append(OptimizedAllocation(
#                 location="Unknown",
#                 disaster_type="Unknown",
#                 impact_level=cluster_instance.get("cluster_label", "Medium"),
#                 cluster_label=cluster_instance.get("cluster_label", "Unknown"),
#                 resource_name=type_dict.get(res_id, "Unknown"),
#                 allocated_resources=allocated_qty
#             ))

#     if allocation_entries:
#         OptimizedAllocation.objects.bulk_create(allocation_entries, batch_size=100)

#     print(f"Optimization Status: {LpStatus[model.status]}")





















































































































# from pulp import LpMaximize, LpProblem, LpVariable, lpSum
# from api.models import DisasterCluster, ResourceData, OptimizedAllocation

# def optimize_resource_allocation():
#     # Step 1: Fetch Clustering Data
#     clustered_disasters = DisasterCluster.objects.all()
#     resource_data = ResourceData.objects.all()

#     # Step 2: Group Data by Cluster Priority
#     cluster_priority = {"High": 1, "Moderate": 2, "Low": 3}  # Lower number = higher priority
#     clustered_disasters = sorted(clustered_disasters, key=lambda d: cluster_priority.get(d.cluster_label, 3))

#     # Step 3: Create Optimization Problem
#     problem = LpProblem("Resource_Allocation", LpMaximize)

#     # Step 4: Define Variables
#     allocation_vars = {
#         (r.resource_id, d.disaster_id): LpVariable(f"alloc_{r.resource_id}_{d.disaster_id}", lowBound=0, cat="Continuous")
#         for r in resource_data for d in clustered_disasters if r.disaster_id == d.disaster.id
#     }

#     # Step 5: Define Objective Function (Maximize total allocated resources)
#     problem += lpSum(allocation_vars.values())

#     # Step 6: Add Constraints
#     for r in resource_data:
#         problem += lpSum(allocation_vars[(r.resource_id, d.disaster.id)] for d in clustered_disasters if (r.resource_id, d.disaster.id) in allocation_vars) <= r.quantity  # Don't exceed available resources

#     # Step 7: Solve the Optimization Problem
#     problem.solve()

#     # Step 8: Store Results in Database
#     OptimizedAllocation.objects.all().delete()  # Clear previous allocations
#     allocations = []
#     for (resource_id, disaster_id), var in allocation_vars.items():
#         if var.varValue > 0:
#             disaster = DisasterCluster.objects.get(disaster_id=disaster_id)
#             resource = ResourceData.objects.get(resource_id=resource_id)
#             allocations.append(OptimizedAllocation(
#                 location=disaster.disaster.location,
#                 disaster_type=disaster.disaster.disaster_type,
#                 impact_level=disaster.cluster_label,
#                 cluster_label=disaster.cluster_label,
#                 resource_name=resource.resource_type,
#                 allocated_resources=var.varValue
#             ))

#     OptimizedAllocation.objects.bulk_create(allocations)
    
#     return "Resource allocation completed successfully."









































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

