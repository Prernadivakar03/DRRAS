
# import csv
# from io import TextIOWrapper
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import (
#     DisasterData,
#     BeneficiaryData,
#     ResourceData,
#     UserInput,
#     OptimizedAllocation,
#     DisasterCluster
# )
# from .serializers import (
#     DisasterDataSerializer,
#     BeneficiaryDataSerializer,
#     ResourceDataSerializer,
#     UserInputSerializer,
#     OptimizedAllocationSerializer
# )
# from .optimization import optimize_resource_allocation
# from .resource_allocation import allocate_resources_with_pulp

# def allocate_resources_userinput_view(request):
#     result = allocate_resources_with_pulp()  # Call the function from resource_allocation.py
#     if "error" in result:
#         return JsonResponse({"error": result["error"]}, status=400)
    
#     return JsonResponse({
#         "message": result["message"],
#         "Allocations": result["Allocations"]
#     }, json_dumps_params={"indent": 4})

# # ✅ Test API Endpoint
# def test_connection(request):
#     return JsonResponse({"message": "Backend is connected to React!"})

# # ✅ ViewSets for Existing Data Models
# class DisasterDataViewSet(viewsets.ModelViewSet):
#     queryset = DisasterData.objects.all()
#     serializer_class = DisasterDataSerializer

# class BeneficiaryDataViewSet(viewsets.ModelViewSet):
#     queryset = BeneficiaryData.objects.all()
#     serializer_class = BeneficiaryDataSerializer

# class ResourceDataViewSet(viewsets.ModelViewSet):
#     queryset = ResourceData.objects.all()
#     serializer_class = ResourceDataSerializer

# # ✅ ViewSet for User-Submitted Disaster Data (Manual Form + CSV)
# class UserInputViewSet(viewsets.ModelViewSet):
#     queryset = UserInput.objects.all()
#     serializer_class = UserInputSerializer

# # ✅ API Endpoint for Running Resource Allocation Optimization
# @api_view(['GET'])
# def run_optimization(request):
#     # Run optimization algorithm
#     optimize_resource_allocation()  

#     # Fetch clusters and resources
#     clusters = DisasterCluster.objects.all().order_by('cluster')  # Prioritize: 0 → 1 → 2
#     resources = ResourceData.objects.all()

#     allocations = []
    
#     # Convert disaster_id to match resource data format (D-xxxx)
#     disaster_id_map = {cluster.disaster_id: f"D-{cluster.disaster_id}" for cluster in clusters}

#     for cluster in clusters:
#         disaster_code = disaster_id_map.get(cluster.disaster_id, None)
#         if not disaster_code:
#             continue  # Skip if no matching disaster code

#         # Filter resources for the given disaster
#         cluster_resources = resources.filter(disaster_id=disaster_code)

#         for resource in cluster_resources:
#             allocations.append({
#                 "location": resource.location,  # Assuming 'id' represents location in DisasterCluster
#                 "cluster_impact": cluster.cluster_label,  # Example: "Severe Impact"
#                 "cluster_no": cluster.cluster,
#                 "resource_name": resource.resource_type,
#                 "quantity": resource.quantity,
#                 "source": cluster.source
#             })

#     response_data = {
#         "message": {
#             "message": "Optimization completed successfully",
#             "allocated_resources": len(allocations)  
#         },
#         "allocations": allocations
#     }

#     return Response(response_data)

# @api_view(['POST'])
# def submit_disaster_data(request):
#     # ✅ Handle Form Data Submission
#     serializer = UserInputSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#         # ✅ Handle CSV File (if present)
#         csv_file = request.FILES.get('csv_file')  # Fixed case
#         if csv_file:
#             try:
#                 file_wrapper = TextIOWrapper(csv_file.file, encoding='utf-8')
#                 reader = csv.DictReader(file_wrapper)

#                 for row in reader:
#                     row = {key.strip(): value.strip() for key, value in row.items()}
#                     csv_serializer = UserInputSerializer(data=row)
#                     if csv_serializer.is_valid():
#                         csv_serializer.save()
#                     else:
#                         return Response({
#                             "error": "CSV Row Error",
#                             "details": csv_serializer.errors
#                         }, status=400)
#                 file_wrapper.close()

#             except Exception as e:
#                 return Response({"error": f"CSV Processing Error: {str(e)}"}, status=400)

#         return Response({
#             "message": "Data submitted successfully!",
#             "data": serializer.data
#         }, status=201)

#     return Response(serializer.errors, status=400)

# # imp 
















































































import csv
from io import TextIOWrapper
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    DisasterData,
    BeneficiaryData,
    ResourceData,
    UserInput,
    OptimizedAllocation,
    DisasterCluster
)
from .serializers import (
    DisasterDataSerializer,
    BeneficiaryDataSerializer,
    ResourceDataSerializer,
    UserInputSerializer,
    OptimizedAllocationSerializer
)
from .optimization import optimize_resource_allocation
from .resource_allocation import allocate_resources_with_pulp

def allocate_resources_userinput_view(request):
    result = allocate_resources_with_pulp()  # Call the function from resource_allocation.py
    if "error" in result:
        return JsonResponse({"error": result["error"]}, status=400)
    
    return JsonResponse({
        "message": result["message"],
        "Allocations": result["Allocations"]
    }, json_dumps_params={"indent": 4})

# ✅ Test API Endpoint
def test_connection(request):
    return JsonResponse({"message": "Backend is connected to React!"})

# ✅ ViewSets for Existing Data Models
class DisasterDataViewSet(viewsets.ModelViewSet):
    queryset = DisasterData.objects.all()
    serializer_class = DisasterDataSerializer

class BeneficiaryDataViewSet(viewsets.ModelViewSet):
    queryset = BeneficiaryData.objects.all()
    serializer_class = BeneficiaryDataSerializer

class ResourceDataViewSet(viewsets.ModelViewSet):
    queryset = ResourceData.objects.all()
    serializer_class = ResourceDataSerializer

# ✅ ViewSet for User-Submitted Disaster Data (Manual Form + CSV)
class UserInputViewSet(viewsets.ModelViewSet):
    queryset = UserInput.objects.all()
    serializer_class = UserInputSerializer

# ✅ API Endpoint for Running Resource Allocation Optimization
@api_view(['GET'])
def run_optimization(request):
    # Run optimization algorithm
    optimize_resource_allocation()  

    # Fetch clusters and resources
    clusters = DisasterCluster.objects.all().order_by('cluster')  # Prioritize: 0 → 1 → 2
    resources = ResourceData.objects.all()

    allocations = []
    
    # Convert disaster_id to match resource data format (D-xxxx)
    disaster_id_map = {cluster.disaster_id: f"D-{cluster.disaster_id}" for cluster in clusters}

    for cluster in clusters:
        disaster_code = disaster_id_map.get(cluster.disaster_id, None)
        if not disaster_code:
            continue  # Skip if no matching disaster code

        # Filter resources for the given disaster
        cluster_resources = resources.filter(disaster_id=disaster_code)

        for resource in cluster_resources:
            allocations.append({
                "location": resource.location,  # Assuming 'id' represents location in DisasterCluster
                "cluster_impact": cluster.cluster_label,  # Example: "Severe Impact"
                "cluster_no": cluster.cluster,
                "resource_name": resource.resource_type,
                "quantity": resource.quantity,
                "source": cluster.source
            })

    response_data = {
        "message": {
            "message": "Optimization completed successfully",
            "allocated_resources": len(allocations)  
        },
        "allocations": allocations
    }

    return Response(response_data)

@api_view(['POST'])
def submit_disaster_data(request):
    # ✅ Handle Form Data Submission
    serializer = UserInputSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # ✅ Handle CSV File (if present)
        csv_file = request.FILES.get('csv_file')  # Fixed case
        if csv_file:
            try:
                file_wrapper = TextIOWrapper(csv_file.file, encoding='utf-8')
                reader = csv.DictReader(file_wrapper)

                for row in reader:
                    row = {key.strip(): value.strip() for key, value in row.items()}
                    csv_serializer = UserInputSerializer(data=row)
                    if csv_serializer.is_valid():
                        csv_serializer.save()
                    else:
                        return Response({
                            "error": "CSV Row Error",
                            "details": csv_serializer.errors
                        }, status=400)
                file_wrapper.close()

            except Exception as e:
                return Response({"error": f"CSV Processing Error: {str(e)}"}, status=400)

        return Response({
            "message": "Data submitted successfully!",
            "data": serializer.data
        }, status=201)

    return Response(serializer.errors, status=400)




@api_view(['PATCH'])
def update_resource_allocation(request, resource_id):
    try:
        resource = ResourceData.objects.get(id=resource_id)
        print(f"Resource found: {resource}")  # Debugging
    except ResourceData.DoesNotExist:
        print(f"Resource ID {resource_id} not found")  # Debugging
        return Response({"error": "Resource not found"}, status=404)

    print(f"Incoming Data: {request.data}")  # Debugging

    serializer = ResourceDataSerializer(resource, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        print(f"Resource updated: {serializer.data}")  # Debugging
        return Response({"message": "Resource updated successfully", "data": serializer.data}, status=200)

    print(f"Serializer Errors: {serializer.errors}")  # Debugging
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def track_resources(request):
    """
    ✅ Fetch live resource tracking details.
    """
    resources = ResourceData.objects.all()
    data = []

    for resource in resources:
        remaining_quantity = resource.quantity - resource.allocated_quantity  # ✅ Fix applied

        data.append({
            "resource_id": resource.resource_id,
            "resource_type": resource.resource_type,
            "total_quantity": resource.quantity,  # ✅ Use `quantity` instead
            "allocated_quantity": resource.allocated_quantity,  
            "remaining_quantity": remaining_quantity,
            "status": resource.status
        })

    return Response({"resources": data})
















