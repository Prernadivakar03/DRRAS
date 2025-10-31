# import pandas as pd
# from django.core.management.base import BaseCommand
# from api.models import Disaster, Beneficiary, Resource
# from datetime import datetime

# class Command(BaseCommand):
#     help = "Load data from CSV files into the database"

#     def handle(self, *args, **kwargs):
#         try:
#             # Load Disaster Data
#             disaster_file = "disaster_data_modified.csv"
#             df_disasters = pd.read_csv(disaster_file)

#             for _, row in df_disasters.iterrows():
#                 Disaster.objects.update_or_create(
#                     disaster_id=row["Disaster ID"],
#                     defaults={
#                         "disaster_type": row["Disaster Type"],
#                         "date": datetime.strptime(row["Date"], "%m/%d/%Y").date(),
#                         "location": row["Location"],
#                         "impact_level": row["Impact Level"],
#                         "people_affected": row["People Affected"],
#                         "casualties": row["Casualties"],
#                         "infrastructure_damage": row["Infrastructure Damage (USD)"],
#                         "relief_resources": row["Relief Resources"],
#                         "response_time": row["Response Time (Hours)"],
#                         "funds_allocated": row["Funds Allocated (USD)"],
#                         "recovery_time": row["Recovery Time (Days)"],
#                     },
#                 )

#             self.stdout.write(self.style.SUCCESS("Successfully loaded Disaster data"))

#             # Load Beneficiary Data
#             beneficiary_file = "beneficiaries.csv"
#             df_beneficiaries = pd.read_csv(beneficiary_file)

#             for _, row in df_beneficiaries.iterrows():
#                 disaster = Disaster.objects.get(disaster_id=row["Disaster ID"])
#                 Beneficiary.objects.update_or_create(
#                     beneficiary_id=row["Beneficiary ID"],
#                     defaults={
#                         "name": row["Name"],
#                         "age": row["Age"],
#                         "gender": row["Gender"],
#                         "location": row["Location"],
#                         "disaster": disaster,
#                     },
#                 )

#             self.stdout.write(self.style.SUCCESS("Successfully loaded Beneficiary data"))

#             # Load Resource Allocation Data
#             resource_file = "resource_allocation.csv"
#             df_resources = pd.read_csv(resource_file)

#             for _, row in df_resources.iterrows():
#                 disaster = Disaster.objects.get(disaster_id=row["Disaster ID"])
#                 beneficiary = Beneficiary.objects.get(beneficiary_id=row["Beneficiary ID"])

#                 Resource.objects.update_or_create(
#                     resource_id=row["Resource ID"],
#                     defaults={
#                         "disaster": disaster,
#                         "resource_type": row["Resource Type"],
#                         "quantity": row["Quantity"],
#                         "allocated_to": beneficiary,
#                     },
#                 )

#             self.stdout.write(self.style.SUCCESS("Successfully loaded Resource Allocation data"))

#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"Error loading data: {e}"))


















# import os
# import csv
# from django.core.management.base import BaseCommand
# from api.models import Disaster, Beneficiary, Resource

# class Command(BaseCommand):
#     help = 'Load disaster, beneficiary, and resource data from CSV files'

#     def handle(self, *args, **kwargs):
#         base_dir = os.path.join(os.path.dirname(__file__), '../../data/')

#         # Load Disaster Data
#         disaster_file = os.path.join(base_dir, 'disaster_data_modified.csv')
#         try:
#             with open(disaster_file, newline='', encoding='utf-8') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     Disaster.objects.create(
#                         name=row["Disaster Type"],
#                         date=row["Date"],
#                         location=row["Location"],
#                         severity=1  # Adjust if needed
#                     )
#             self.stdout.write(self.style.SUCCESS('✅ Successfully loaded disaster data'))
#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"❌ Error loading disaster data: {e}"))

#         # Load Beneficiary Data
#         beneficiary_file = os.path.join(base_dir, 'beneficiaries.csv')
#         try:
#             with open(beneficiary_file, newline='', encoding='utf-8') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     disaster = Disaster.objects.filter(name=row["Disaster Type"]).first()
#                     Beneficiary.objects.create(
#                         name=row["Beneficiary Name"],
#                         location=row["Location"],
#                         disaster=disaster,
#                         assistance_received=row.get("Assistance Received", "")
#                     )
#             self.stdout.write(self.style.SUCCESS('✅ Successfully loaded beneficiary data'))
#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"❌ Error loading beneficiary data: {e}"))

#         # Load Resource Data
#         resource_file = os.path.join(base_dir, 'resource_allocation.csv')
#         try:
#             with open(resource_file, newline='', encoding='utf-8') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 for row in reader:
#                     disaster = Disaster.objects.filter(name=row["Disaster Type"]).first()
#                     beneficiary = Beneficiary.objects.filter(name=row["Beneficiary Name"]).first()
#                     Resource.objects.create(
#                         name=row["Resource Type"],
#                         quantity=int(row["Quantity"]),
#                         disaster=disaster,
#                         allocated_to=beneficiary
#                     )
#             self.stdout.write(self.style.SUCCESS('✅ Successfully loaded resource data'))
#         except Exception as e:
#             self.stderr.write(self.style.ERROR(f"❌ Error loading resource data: {e}"))







import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import DisasterData, BeneficiaryData, ResourceData

class Command(BaseCommand):
    help = "Load CSV data into DisasterData, BeneficiaryData, and ResourceData models"

    def handle(self, *args, **options):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))

        # Load Disaster Data
        self.load_csv("disaster_data_modified_updated.csv", base_path, self.load_disaster_data, "DisasterData")
        # Load Beneficiary Data
        self.load_csv("beneficiaries_updated.csv", base_path, self.load_beneficiary_data, "BeneficiaryData")
        # Load Resource Data
        self.load_csv("resource_allocation_updated.csv", base_path, self.load_resource_data, "ResourceData")

    def load_csv(self, filename, base_path, loader_function, model_name):
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            try:
                loader_function(filepath)
                self.stdout.write(self.style.SUCCESS(f"✅ Successfully loaded {model_name} from {filename}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error loading {model_name}: {e}"))
        else:
            self.stdout.write(self.style.ERROR(f"❌ {model_name} CSV not found: {filepath}"))

    def parse_date(self, date_str):
        """Convert date from MM/DD/YYYY to YYYY-MM-DD format"""
        try:
            return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return "2023-01-01"  # Default fallback date in case of errors

    def load_disaster_data(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            DisasterData.objects.bulk_create([
                DisasterData(
                    disaster_id=row.get("Disaster ID", ""),
                    disaster_type=row.get("Disaster Type", ""),
                    date=self.parse_date(row.get("Date", "01/01/2023")),  # Convert date
                    location=row.get("Location", ""),
                    impact_level=row.get("Impact Level", ""),
                    people_affected=int(row.get("People Affected", 0)),
                    casualties=int(row.get("Casualties", 0)),
                    infrastructure_damage_usd=float(row.get("Infrastructure Damage (USD)", 0)),
                    relief_resources=row.get("Relief Resources", ""),
                    response_time_hours=int(row.get("Response Time (Hours)", 0)),
                    funds_allocated_usd=float(row.get("Funds Allocated (USD)", 0)),
                    recovery_time_days=int(row.get("Recovery Time (Days)", 0))
                ) for row in reader
            ])

    def load_beneficiary_data(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            BeneficiaryData.objects.bulk_create([
                BeneficiaryData(
                    beneficiary_id=row.get("Beneficiary ID", ""),
                    disaster_id=row.get("Disaster ID", ""),
                    name=row.get("Name", ""),
                    age=int(row.get("Age", 0)),
                    gender=row.get("Gender", ""),
                    location=row.get("Location", ""),
                    aid_received=row.get("Aid Received", ""),
                    date_received=self.parse_date(row.get("Date Received", "01/01/2023"))  # Convert date
                ) for row in reader
            ])

    def load_resource_data(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            ResourceData.objects.bulk_create([
                ResourceData(
                    resource_id=row.get("Resource ID", ""),
                    disaster_id=row.get("Disaster ID", ""),
                    resource_type=row.get("Resource Type", ""),
                    quantity=int(row.get("Quantity", 0)),
                    cost_usd=float(row.get("Cost (USD)", 0)),
                    deployment_date=self.parse_date(row.get("Deployment Date", "01/01/2023")),  # Convert date
                    location=row.get("Location", ""),
                    status=row.get("Status", "")
                ) for row in reader
            ])
