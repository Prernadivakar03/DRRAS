
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from django.http import JsonResponse
from .models import DisasterData, DisasterCluster, UserInput, UserDisasterCluster

def disaster_clustering(request):
    try:
        # ✅ Fetch disaster data from DisasterData model
        disasters = DisasterData.objects.all().values(
            "id", "location", "disaster_type", "people_affected", 
            "casualties", "infrastructure_damage_usd", "funds_allocated_usd"
        )

        # ✅ Fetch user-inputted disaster data from UserInput model
        user_disasters = UserInput.objects.all().values(
            "id", "location", "disaster_type", "people_affected", 
            "casualties", "infrastructure_damage", "funds_allocated"
        )

        # ✅ Convert to DataFrame
        df_disasters = pd.DataFrame(list(disasters))
        df_user_disasters = pd.DataFrame(list(user_disasters))

        # ✅ Add 'source' column to identify data origin
        df_disasters["source"] = "disaster_data"
        df_user_disasters["source"] = "user_input"

        # ✅ Standardize column names for merging
        if not df_user_disasters.empty:
            df_user_disasters.rename(
                columns={"infrastructure_damage": "infrastructure_damage_usd", "funds_allocated": "funds_allocated_usd"},
                inplace=True
            )

        # ✅ Combine both datasets
        df = pd.concat([df_disasters, df_user_disasters], ignore_index=True)

        # ✅ Define core features for clustering
        features = ["people_affected", "casualties", "infrastructure_damage_usd", "funds_allocated_usd"]

        # ✅ Fill missing values with default numbers (prevent errors)
        df[features] = df[features].apply(pd.to_numeric, errors="coerce")  # Convert to numeric
        df[features] = df[features].fillna(0)  # Replace NaN with zero

        # ✅ If all values are 0, return an error
        if df[features].sum().sum() == 0:
            return JsonResponse({"error": "No meaningful data available for clustering. Please check your inputs."}, status=400)

        # ✅ Normalize data for better clustering
        df[features] = (df[features] - df[features].mean()) / df[features].std()

        # ✅ Apply K-Means Clustering
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df["Cluster"] = kmeans.fit_predict(df[features])

        # ✅ Assign Impact Levels Based on Cluster
        impact_mapping = {0: "Severe Impact", 1: "Moderate Impact", 2: "Low Impact"}
        df["Impact Level"] = df["Cluster"].map(impact_mapping)

        # ✅ Clear old cluster data
        DisasterCluster.objects.all().delete()
        UserDisasterCluster.objects.all().delete()

        # ✅ Store clustered data in the correct table
        for _, row in df.iterrows():
            if row["source"] == "disaster_data":
                DisasterCluster.objects.create(
                    disaster_id=row["id"],  # ✅ DisasterData uses disaster_id
                    cluster=row["Cluster"],
                    cluster_label=row["Impact Level"],
                    source=row["source"]
                )
            elif row["source"] == "user_input":
                UserDisasterCluster.objects.create(  # ✅ UserInput uses user_disaster_id
                    user_disaster_id=row["id"],  # 🚨 FIX: Changed from `disaster_id` to `user_disaster_id`
                    cluster=row["Cluster"],
                    cluster_label=row["Impact Level"],
                    source=row["source"]
                )

        # ✅ Convert full dataset to JSON format
        full_clustered_data = df.to_dict(orient="records")

        # ✅ Compute summary statistics for each cluster
        cluster_summary = df.groupby("Impact Level")[features].mean().round(2).to_dict(orient="index")

        return JsonResponse({
            "Clustered Data": full_clustered_data,
            "Cluster Summary": cluster_summary,
            "Cluster Centers": kmeans.cluster_centers_.tolist()
        }, json_dumps_params={"indent": 4})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)








































