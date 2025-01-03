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
  ![image](https://in.images.search.yahoo.com/yhs/search;_ylt=AwrPrWvWO3hn59o8iRMO9olQ;_ylu=c2VjA3NlYXJjaARzbGsDYXNzaXN0;_ylc=X1MDMTM1MTIxODcwMgRfcgMyBGZyA3locy1zei0wMDIEZnIyA3NhLWdwLXNlYXJjaARncHJpZANFMmcxNDhIOVEuMnZ5dEdJVWFtS3JBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzEEcHFzdHIDZWxvYm93IGdyBHBxc3RybAM5BHFzdHJsAzExBHF1ZXJ5A2VsYm93JTIwZ3JhcGgEdF9zdG1wAzE3MzU5MzU2MDMEdXNlX2Nhc2UD?p=elbow+graph&fr=yhs-sz-002&fr2=sa-gp-search&ei=UTF-8&x=wrt&type=type80160-3464885101&hsimp=yhs-002&hspart=sz&param1=454896003&vm=r#id=19&iurl=https%3A%2F%2Fav-eks-blogoptimized.s3.amazonaws.com%2F83750elbow.png&action=click)
