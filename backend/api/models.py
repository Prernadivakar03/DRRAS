

# from django.db import models
# from django.core.exceptions import ValidationError
# from django.contrib.auth.hashers import make_password, check_password

# # Model to store Disaster CSV data
# class DisasterData(models.Model):
#     disaster_id = models.CharField(max_length=50)
#     disaster_type = models.CharField(max_length=255)
#     date = models.DateField()
#     location = models.CharField(max_length=255)
#     impact_level = models.CharField(max_length=50)
#     people_affected = models.IntegerField()
#     casualties = models.IntegerField()
#     infrastructure_damage_usd = models.FloatField()
#     relief_resources = models.CharField(max_length=255)
#     response_time_hours = models.IntegerField()
#     funds_allocated_usd = models.FloatField()
#     recovery_time_days = models.IntegerField()

#     def __str__(self):
#         return f"{self.disaster_id} - {self.disaster_type}"

# # Model to store Beneficiary CSV data
# class BeneficiaryData(models.Model):
#     beneficiary_id = models.CharField(max_length=50)
#     disaster_id = models.CharField(max_length=50)
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=50)
#     location = models.CharField(max_length=255)
#     aid_received = models.CharField(max_length=255)
#     date_received = models.DateField()

#     def __str__(self):
#         return f"{self.beneficiary_id} - {self.name}"

# # Model to store Resource CSV data
# class ResourceData(models.Model):
#     resource_id = models.CharField(max_length=50)
#     disaster_id = models.CharField(max_length=50)
#     resource_type = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     cost_usd = models.FloatField()
#     deployment_date = models.DateField()
#     location = models.CharField(max_length=255)
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.resource_id} - {self.resource_type}"

# class DisasterCluster(models.Model):
#     disaster = models.ForeignKey(DisasterData, on_delete=models.CASCADE)
#     cluster = models.IntegerField()
#     cluster_label = models.CharField(max_length=50)
#     source = models.CharField(
#         max_length=20,
#         choices=[("disaster_data", "DisasterData"), ("userinput", "UserInput")]
#     )

#     def __str__(self):
#         return f"{self.disaster.location} - {self.cluster_label}"

# # ✅ Store User Input Data (Manual & CSV)
# class UserInput(models.Model):
#     disaster_type = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     people_affected = models.IntegerField()
#     infrastructure_damage = models.FloatField()
#     funds_allocated = models.FloatField()
#     casualties = models.IntegerField()
#     resource_name = models.CharField(max_length=255)
#     date = models.DateField(auto_now_add=True)
#     csv_file = models.FileField(upload_to="uploads/", blank=True, null=True)

#     def __str__(self):
#         return f"{self.disaster_type} - {self.location}"

# # ✅ **New Model: Store Optimized Resource Allocation Results**
# class OptimizedAllocation(models.Model):
#     location = models.CharField(max_length=255)
#     disaster_type = models.CharField(max_length=255)
#     cluster_label = models.CharField(max_length=50)
#     resource_name = models.CharField(max_length=255)  # ✅ Store resource name
#     allocated_resources = models.FloatField()


#     def __str__(self):
#         return f"{self.location} - {self.resource_name} - {self.allocated_resources}"



# # ✅ User-Submitted Disaster Clustering Model (for UserInput)
# class UserDisasterCluster(models.Model):
#     user_disaster = models.ForeignKey(UserInput, on_delete=models.CASCADE)
#     cluster = models.IntegerField()
#     cluster_label = models.CharField(max_length=50)
#     source = models.CharField(
#         max_length=20,
#         choices=[("userinput", "UserInput")], default="userinput"
#     )

#     def __str__(self):
#         return f"{self.user_disaster.location} - {self.cluster_label}"
    

# class Volunteer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     password = models.CharField(max_length=100)  # Accepts any combination of numbers, characters, and symbols
#     availability = models.TextField(blank=True, null=True)
#     skills = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name












































from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Model to store Disaster CSV data
class DisasterData(models.Model):
    disaster_id = models.CharField(max_length=50)
    disaster_type = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    impact_level = models.CharField(max_length=50)
    people_affected = models.IntegerField()
    casualties = models.IntegerField()
    infrastructure_damage_usd = models.FloatField()
    relief_resources = models.CharField(max_length=255)
    response_time_hours = models.IntegerField()
    funds_allocated_usd = models.FloatField()
    recovery_time_days = models.IntegerField()

    def __str__(self):
        return f"{self.disaster_id} - {self.disaster_type}"

# Model to store Beneficiary CSV data
class BeneficiaryData(models.Model):
    beneficiary_id = models.CharField(max_length=50)
    disaster_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    aid_received = models.CharField(max_length=255)
    date_received = models.DateField()

    def __str__(self):
        return f"{self.beneficiary_id} - {self.name}"

# Model to store Resource CSV data
class ResourceData(models.Model):
    resource_id = models.CharField(max_length=50)
    disaster_id = models.CharField(max_length=50)
    resource_type = models.CharField(max_length=255)
    quantity = models.IntegerField()  # Total available resources
    allocated_quantity = models.IntegerField(default=0)  # ✅ New: Tracks how much is used
    cost_usd = models.FloatField()
    deployment_date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    @property
    def remaining_quantity(self):
        return self.quantity - self.allocated_quantity  # ✅ Dynamically calculates remaining resources

    def __str__(self):
        return f"{self.resource_id} - {self.resource_type} - Remaining: {self.remaining_quantity}"


class DisasterCluster(models.Model):
    disaster = models.ForeignKey(DisasterData, on_delete=models.CASCADE)
    cluster = models.IntegerField()
    cluster_label = models.CharField(max_length=50)
    source = models.CharField(
        max_length=20,
        choices=[("disaster_data", "DisasterData"), ("userinput", "UserInput")]
    )

    def __str__(self):
        return f"{self.disaster.location} - {self.cluster_label}"

# ✅ Store User Input Data (Manual & CSV)
class UserInput(models.Model):
    disaster_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    people_affected = models.IntegerField()
    infrastructure_damage = models.FloatField()
    funds_allocated = models.FloatField()
    casualties = models.IntegerField()
    resource_name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    csv_file = models.FileField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"{self.disaster_type} - {self.location}"

# ✅ **New Model: Store Optimized Resource Allocation Results**
class OptimizedAllocation(models.Model):
    location = models.CharField(max_length=255)
    disaster_type = models.CharField(max_length=255)
    cluster_label = models.CharField(max_length=50)
    resource_name = models.CharField(max_length=255)  # ✅ Store resource name
    allocated_resources = models.FloatField()


    def __str__(self):
        return f"{self.location} - {self.resource_name} - {self.allocated_resources}"



# ✅ User-Submitted Disaster Clustering Model (for UserInput)
class UserDisasterCluster(models.Model):
    user_disaster = models.ForeignKey(UserInput, on_delete=models.CASCADE)
    cluster = models.IntegerField()
    cluster_label = models.CharField(max_length=50)
    source = models.CharField(
        max_length=20,
        choices=[("userinput", "UserInput")], default="userinput"
    )

    def __str__(self):
        return f"{self.user_disaster.location} - {self.cluster_label}"
    

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # Accepts any combination of numbers, characters, and symbols
    availability = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name