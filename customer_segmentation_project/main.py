import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# =====================================================================
# STEP 1: LOAD THE DATASET
# =====================================================================
print("--- Step 1: Loading Dataset ---")
# Using ISO-8859-1 encoding to handle special characters smoothly
df = pd.read_csv('OnlineRetail.csv', encoding='ISO-8859-1')

print(f"Dataset Shape: {df.shape}")
print("\nDataset Information Summary:")
print(df.info())


# =====================================================================
# STEP 2: CLEAN DATA
# =====================================================================
print("\n--- Step 2: Cleaning Missing and Invalid Data ---")

# 1. Remove rows where CustomerID is missing
df = df.dropna(subset=['CustomerID'])

# 2. Create a total spending column (Quantity * UnitPrice)
df['TotalSum'] = df['Quantity'] * df['UnitPrice']

# 3. Filter out negative or zero quantities and prices (removes returns/errors)
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

print(f"Cleaned Dataset Shape: {df.shape}")


# =====================================================================
# STEP 3: FEATURE ENGINEERING (RFM)
# =====================================================================
print("\n--- Step 3: Engineering RFM Metrics ---")

# 1. Convert InvoiceDate column to a proper datetime object
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 2. Establish a snapshot date (1 day after the latest transaction in the data)
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# 3. Compress transaction history into a single customer matrix
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',                                  # Frequency
    'TotalSum': 'sum'                                         # Monetary
})

# 4. Rename columns for clear identification
rfm.rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'TotalSum': 'Monetary'
}, inplace=True)

print("\nEngineered RFM Dataframe (First 5 Rows):")
print(rfm.head())


# =====================================================================
# STEP 4: DATA TRANSFORMATION & SCALING
# =====================================================================
print("\n--- Step 4: Handling Skewness and Scaling ---")

# 1. Apply log transformation to manage right-skewed metric distributions
rfm_log = np.log1p(rfm)

# 2. Scale features to keep variance balanced for K-Means clustering
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# Preview scaled matrix structure via DataFrame
rfm_scaled_df = pd.DataFrame(rfm_scaled, index=rfm.index, columns=rfm.columns)
print("\nNormalized Data Matrix (First 5 Rows):")
print(rfm_scaled_df.head())


# =====================================================================
# STEP 5: ELBOW METHOD TO FIND OPTIMAL K
# =====================================================================
print("\n--- Step 5: Generating Elbow Method Plot ---")

wcss = []
# Calculate within-cluster sum of squares for K values between 1 and 10
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(rfm_scaled)
    wcss.append(kmeans.inertia_)

# Generate the interactive visualization window
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='b')
plt.title('The Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Inertia)')
plt.grid(True)
print("-> Displaying Elbow Curve. Close the window screen to continue code execution.")
plt.show()


# =====================================================================
# STEP 6: TRAIN FINAL MODEL AND ANALYZE TARGET SEGMENTS
# =====================================================================
print("\n--- Step 6: Running Final K-Means & Profiling ---")

# Standard benchmark setting for retail segmentation data using 3 clusters
chosen_clusters = 3
kmeans_final = KMeans(n_clusters=chosen_clusters, init='k-means++', random_state=42)
kmeans_final.fit(rfm_scaled)

# Assign cluster codes back to our core unscaled customer list
rfm['Cluster'] = kmeans_final.labels_

# Uncover consumer identities by tracking cluster averages
cluster_profile = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).reset_index()

# Attach total member weights per user pocket
cluster_profile['Customer Count'] = rfm.groupby('Cluster').size().values

print("\n================================================")
print("       FINAL CUSTOMER SEGMENT PROFILES          ")
print("================================================")
print(cluster_profile.to_string(index=False))
print("================================================")