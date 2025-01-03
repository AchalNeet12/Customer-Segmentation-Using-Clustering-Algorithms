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
- The Elbow Method is used to determine the optimal number of clusters in the K-Means clustering algorithm. The method involves plotting the Within-Cluster Sum of Squares (WCSS) against the number of clusters. 
  The point where the decrease in WCSS starts to slow down (forming an "elbow" shape) is considered the optimal number of clusters. This helps in selecting the number of clusters that balances cluster quality 
  and computational efficiency.
  ![image](https://github.com/user-attachments/assets/15ef014b-cdda-4c2b-9bba-6f5e7c80fe37)
