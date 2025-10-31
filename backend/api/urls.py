

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     test_connection,
#     DisasterDataViewSet,
#     BeneficiaryDataViewSet,
#     ResourceDataViewSet,
#     UserInputViewSet,  # ✅ Added UserInputViewSet
#     run_optimization
# )
# from .clustering import disaster_clustering
# from api.views import run_optimization
# from .views import allocate_resources_with_pulp



# # ✅ Initialize Router
# router = DefaultRouter()
# router.register(r'disasters', DisasterDataViewSet, basename='disaster')
# router.register(r'beneficiaries', BeneficiaryDataViewSet, basename='beneficiary')
# router.register(r'resources', ResourceDataViewSet, basename='resource')
# router.register(r'userinput', UserInputViewSet, basename='userinput')  # ✅ Added this

# # ✅ Define URL Patterns
# urlpatterns = [
#     path("test/", test_connection, name="test_connection"),
#     path("", include(router.urls)),  # API endpoints
#     path('cluster/', disaster_clustering, name='disaster_clustering'),
#     path('run-optimization/', run_optimization, name='run_optimization'),
#     path("allocate-resources/", allocate_resources_with_pulp, name="allocate_resources"),

    
# ]
# #impcode 
















from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    test_connection,
    DisasterDataViewSet,
    BeneficiaryDataViewSet,
    ResourceDataViewSet,
    UserInputViewSet,
    run_optimization,
    allocate_resources_with_pulp,
    update_resource_allocation,  # ✅ Added function
    track_resources  # ✅ Added function
)
from .clustering import disaster_clustering

# ✅ Initialize Router
router = DefaultRouter()
router.register(r'disasters', DisasterDataViewSet, basename='disaster')
router.register(r'beneficiaries', BeneficiaryDataViewSet, basename='beneficiary')
router.register(r'resources', ResourceDataViewSet, basename='resource')
router.register(r'userinput', UserInputViewSet, basename='userinput')

# ✅ Define URL Patterns
urlpatterns = [
    path("test/", test_connection, name="test_connection"),
    path("", include(router.urls)),  
    path('cluster/', disaster_clustering, name='disaster_clustering'),
    path('run-optimization/', run_optimization, name='run_optimization'),
    path("allocate-resources/", allocate_resources_with_pulp, name="allocate_resources"),

    # ✅ New Endpoints for Resource Tracking & Updates
    path("track-resources/", track_resources, name="track_resources"),
    path('update-resource/<int:resource_id>/', update_resource_allocation, name="update_resource"),

]
