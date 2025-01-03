import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import streamlit as st
import base64
from sklearn.metrics import silhouette_score

# Function to read and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Set the background image using CSS
def set_background(image_base64):
    page_bg_img = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .stMarkdownContainer {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }}
    .stButton > button {{
        background-color: #4C4C6D;
        color: white;
        border-radius: 10px;
        font-size: 16px;
    }}
    .stButton > button:hover {{
        background-color: #6A5ACD;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up background
image_base64 = get_base64_image("Backgroungimg.jpg")  # Update the path to your background image
set_background(image_base64)

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")
data = df.iloc[:, [3, 4]].values  # Annual Income and Spending Score

# K-Means prediction function
def predict_kmeans_cluster(income, spending):
    kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
    kmeans.fit(data)
    input_data = np.array([[income, spending]])
    cluster = kmeans.predict(input_data)
    return cluster[0]

# App layout
st.markdown("<h2 style='text-align: center; color: white;'> Customer Segmentation Analyzer </h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>This app predicts the customer cluster based on Annual Income and Spending Score</p>", unsafe_allow_html=True)

# User inputs
st.markdown("<h4 style='color: white;'>Input Customer Data</h4>", unsafe_allow_html=True)
income = st.slider("Annual Income ($k)", min_value=0, max_value=200, value=50)
spending = st.slider("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# K-Means Clustering
st.markdown("<h4 style='color: white;'>K-Means Clustering Visualization</h4>", unsafe_allow_html=True)
if st.button("Run K-Means Clustering"):
    # K-Means clustering
    kmeans = KMeans(n_clusters=5, init="k-means++", random_state=0)
    y_kmeans = kmeans.fit_predict(data)

    # Visualization
    plt.figure(figsize=(10, 6))
    for i in range(5):
        plt.scatter(data[y_kmeans == i, 0], data[y_kmeans == i, 1], s=100, label=f"Cluster {i+1}")
    plt.scatter(income, spending, s=200, c="orange", label="Input Data Point", edgecolor="black")
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c="black", label="Centroids")
    plt.title("K-Means Clustering")
    plt.xlabel("Annual Income ($k)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    st.pyplot(plt)

    # Predict cluster for input data
    cluster = predict_kmeans_cluster(income, spending)
    st.write(f"Customer belongs to **Cluster {cluster + 1}** (based on K-Means).")

# Hierarchical Clustering
st.markdown("<h4 style='color: white;'>Hierarchical Clustering</h4>", unsafe_allow_html=True)
if st.button("Run Hierarchical Clustering"):
    # Hierarchical clustering visualization
    dendrogram = sch.dendrogram(sch.linkage(data, method="ward"))
    plt.figure(figsize=(10, 6))
    sch.dendrogram(sch.linkage(data, method="ward"))
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Customers")
    plt.ylabel("Euclidean Distance")
    st.pyplot(plt)

    # Fit and predict using Agglomerative Clustering
    hc = AgglomerativeClustering(n_clusters=5, metric="euclidean", linkage="ward")
    y_hc = hc.fit_predict(data)

    # Visualization
    plt.figure(figsize=(10, 6))
    for i in range(5):
        plt.scatter(data[y_hc == i, 0], data[y_hc == i, 1], s=100, label=f"Cluster {i+1}")
    plt.scatter(income, spending, s=200, c="orange", label="Input Data Point", edgecolor="black")
    plt.title("Hierarchical Clustering")
    plt.xlabel("Annual Income ($k)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    st.pyplot(plt)

    # Predict cluster for input data
    input_data = np.array([[income, spending]])
    hc_cluster = hc.fit_predict(np.vstack([data, input_data]))[-1]
    st.write(f"Customer belongs to **Cluster {hc_cluster + 1}** (based on Hierarchical Clustering).")
