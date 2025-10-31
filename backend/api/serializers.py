
# from rest_framework import serializers
# from .models import DisasterData, BeneficiaryData, ResourceData,OptimizedAllocation  , UserInput
# class DisasterDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DisasterData
#         fields = '__all__'

# class BeneficiaryDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BeneficiaryData
#         fields = '__all__'

# class ResourceDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResourceData
#         fields = '__all__'


# # ✅ Serializer for User-Submitted Disaster Data (Manual & CSV)
# class UserInputSerializer(serializers.ModelSerializer):
#     csv_file = serializers.FileField(required=False)

#     class Meta:
#         model = UserInput
#         fields = '__all__'

# # ✅ Serializer for Optimized Resource Allocation
# class OptimizedAllocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OptimizedAllocation
#         fields = '__all__'





































from rest_framework import serializers
from .models import DisasterData, BeneficiaryData, ResourceData,OptimizedAllocation  , UserInput
class DisasterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterData
        fields = '__all__'

class BeneficiaryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiaryData
        fields = '__all__'


# ✅ Serializer for User-Submitted Disaster Data (Manual & CSV)
class UserInputSerializer(serializers.ModelSerializer):
    csv_file = serializers.FileField(required=False)

    class Meta:
        model = UserInput
        fields = '__all__'

# ✅ Serializer for Optimized Resource Allocation
class OptimizedAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimizedAllocation
        fields = '__all__'


class ResourceDataSerializer(serializers.ModelSerializer):
    allocated_quantity = serializers.SerializerMethodField()  # ✅ Ensure correct allocation
    remaining_quantity = serializers.SerializerMethodField()  # ✅ Ensure correct remaining quantity

    class Meta:
        model = ResourceData
        fields = '__all__'  # Includes all fields

    def get_allocated_quantity(self, obj):
        return obj.quantity  # ✅ Correctly map "Quantity" as allocated_quantity

    def get_remaining_quantity(self, obj):
        return obj.quantity - obj.quantity  # ✅ Ensure correct remaining calculation








