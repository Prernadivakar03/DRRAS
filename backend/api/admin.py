# from django.contrib import admin
# from .models import Disaster, Resource

# admin.site.register(Disaster)
# admin.site.register(Resource)
#imp above






from django.contrib import admin
from .models import DisasterData, BeneficiaryData, ResourceData

@admin.register(DisasterData)
class DisasterDataAdmin(admin.ModelAdmin):
    list_display = ("disaster_id", "disaster_type", "date", "location")

@admin.register(BeneficiaryData)
class BeneficiaryDataAdmin(admin.ModelAdmin):
    list_display = ("beneficiary_id", "name", "disaster_id", "location")

@admin.register(ResourceData)
class ResourceDataAdmin(admin.ModelAdmin):
    list_display = ("resource_id", "resource_type", "disaster_id", "quantity")
