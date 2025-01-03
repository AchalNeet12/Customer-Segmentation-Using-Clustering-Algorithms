# Customer Segmentation Using Clustering Algorithms
---
## 📜 Overview:
  - Customer segmentation is the process of dividing customers into different groups based on certain characteristics. This helps businesses tailor their strategies for marketing, sales, and product offerings.
    In  this project, we applied two unsupervised learning algorithms—K-Means Clustering and Hierarchical Clustering—to segment customers based on their Annual Income and Spending Score. 
  - The goal is to understand customer behavior and predict which cluster a new customer would fall into, based on their income and spending score. Both clustering algorithms were used to compare the 
    segmentation results and understand how different approaches affect the grouping.
---
## 📦 Dataset:   
 The dataset used in this project is the Mall Customers Dataset, which contains the following columns:

- `CustomerID`: Unique identifier for each customer.
- `Gender`: Gender of the customer.
- `Age`: Age of the customer.
- `Annual Income (k$)`: Annual income of the customer (in thousands of dollars).
- `Spending Score (1-100)`: Score assigned based on customer spending behavior, ranging from 1 to 100.
  
For clustering purposes, we used only the Annual Income (k$) and Spending Score (1-100) columns.
---
## ⬛ Elbow Method:
- The Elbow Method is used to determine the optimal number of clusters in the K-Means clustering algorithm. The method involves plotting the Within-Cluster Sum of Squares (WCSS) against the number of 
  clusters. The point where the decrease in WCSS starts to slow down (forming an "elbow" shape) is considered the optimal number of clusters. This helps in selecting the number of clusters that balances 
  cluster quality and computational efficiency.
  
  ![image](https://github.com/user-attachments/assets/15ef014b-cdda-4c2b-9bba-6f5e7c80fe37)
---
## ⬛ K-Means Clustering:
- K-Means is an iterative algorithm that divides the data into K clusters by minimizing the sum of squared distances between data points and their cluster centroids. The algorithm works as follows:

    - Initialize K centroids (either randomly or using a method like K-Means++).
    - Assign each data point to the nearest centroid.
    - Recalculate the centroids based on the mean of assigned points.
    - Repeat the assignment and centroid calculation steps until convergence (i.e., the centroids no longer move significantly).
      
K-Means requires the number of clusters (K) to be specified beforehand, and the results are influenced by the initial centroids.

![K-Means Clustering](https://editor.analyticsvidhya.com/uploads/94062graph%20cluster.png)
---
## ⬛ Hierarchical Clustering:
- Hierarchical Clustering builds a hierarchy of clusters, starting from each data point as its own cluster and progressively merging the closest clusters. It does not require specifying the number of clusters 
  upfront. The main steps are:

    - Agglomerative (bottom-up): Begin with individual data points and merge the closest pairs.

![Agglomerative Clustering](https://github.com/user-attachments/assets/c52df549-1e1f-4f79-ae0a-4ff5ba878937)

A scatter plot was generated similar to the K-Means visualization, showing the 5 clusters formed by **Hierarchical Clustering**.

![image](https://github.com/user-attachments/assets/f42c9526-74e5-4e6a-afe1-9ccdce97684d)

   - Divisive (top-down): Start with one large cluster and iteratively divide it into smaller ones.

- A dendrogram is used to visualize the hierarchical clustering process, where the distance between merged clusters is shown.
---
## 🤖 Technology:
 - `Python`: Programming language used for the project.
 - Libraries:
  - `Pandas`: For data manipulation.
  - `Numpy`: For numerical operations. 
  - `Matplotlib` and `Seaborn`: For data visualization.
  - `Scikit-learn`: For K-Means and Hierarchical Clustering models.
  - `Streamlit`: For building the web app interface.
---
## 🔍 Data Preprocessing:
 - **Handling Missing Values**: There were no missing values in the dataset, so no imputation was needed.
 - **Feature Selection**: Only the Annual Income and Spending Score were used for clustering, as these are the key factors in customer segmentation.
 - **Scaling**: Although K-Means is sensitive to scaling, the dataset used already had relatively well-distributed values for the selected features, so scaling was not applied in this 
   case.
---
## ⚙ Model:
 - K-Means Clustering:
   - The number of clusters was selected using the Elbow Method.
   - We trained the K-Means model with 5 clusters and visualized the clusters using a scatter plot.
 - Hierarchical Clustering:
   - A dendrogram was used to visualize the hierarchical structure.
   - We used Agglomerative Clustering with 5 clusters and visualized the clusters with a scatter plot.
---
## 📈 Results:
   - K-Means: Segmented the customers into 5 distinct groups based on their income and spending behavior. Each cluster was represented by a different color in the scatter plot.
   - Hierarchical Clustering: Provided a similar segmentation result, but the clusters might slightly differ in shape due to the algorithm's different approach.
    
- Both algorithms were able to predict the same general cluster structure, but there were minor differences due to how they define clusters.
---
## 📊 Conclusion:
 - Both K-Means and Hierarchical Clustering were effective for segmenting the customers based on their Annual Income and Spending Score. However, the algorithms produced slightly 
   different results due to their different approaches to clustering:
       - K-Means is more suited for large datasets with spherical clusters.
       - Hierarchical Clustering provides a more detailed view of the cluster hierarchy and does not require the number of clusters to be predefined.
 - The choice between these algorithms depends on the dataset and the specific problem requirements. If the number of clusters is known, K-Means is faster and more efficient, while 
   Hierarchical Clustering is better for exploring data and understanding hierarchical relationships.
---
## 🌐 STREAMLIT FRONTEND **(You can access the Streamlit app)**





