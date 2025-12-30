
#  Customer Segmentation using K-Means Clustering

##  Project Overview

This project implements **K-Means clustering** to segment customers of a retail store based on their purchasing behavior.
The goal is to group customers with similar characteristics so businesses can better understand and target their customers.

This project was developed as part of **ProDigy Infotech – Machine Learning Internship (Task 02)**.

---

##  Objective

* To apply **unsupervised machine learning** for customer segmentation
* To identify distinct customer groups based on:

  * Annual Income
  * Spending Score
* To visualize customer segments using a scatter plot

---

##  Dataset

**Dataset Name:** Mall Customers Dataset
**Source:** Kaggle

**Features used:**

* `CustomerID`
* `Gender`
* `Age`
* `Annual Income (k$)`
* `Spending Score (1–100)`

For clustering, only:

* **Annual Income (k$)**
* **Spending Score (1–100)**
  are used.

---

##  Machine Learning Algorithm

### K-Means Clustering

* Type: **Unsupervised Learning**
* Number of clusters: **5**
* Purpose: Group customers with similar purchasing behavior

K-Means automatically assigns each customer to the nearest cluster based on similarity.

---

##  Technologies Used

* **Python**
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **Scikit-learn** – K-Means clustering

---

##  Project Structure

```
customer_segmentation_ml/
├── customer_segmentation.py
├── Mall_Customers.csv
└── README.md
```

---

##  How to Run the Project

### Step 1: Install required libraries

```bash
pip install pandas numpy matplotlib scikit-learn
```

### Step 2: Run the program

```bash
python customer_segmentation.py
```

---

## Output

* A **scatter plot** showing customer clusters
* Each point represents a customer
* Different colors represent different customer segments

**Axes:**

* X-axis: Annual Income (k$)
* Y-axis: Spending Score (1–100)

---

##  Interpretation of Clusters

The clusters represent different types of customers, such as:

* High income – high spending customers (premium customers)
* High income – low spending customers
* Low income – high spending customers
* Low income – low spending customers
* Average income – average spending customers

These insights help businesses design targeted marketing strategies.

---

##  Use Case

Retail businesses can use this segmentation to:

* Identify premium customers
* Offer personalized discounts
* Improve marketing strategies
* Increase customer satisfaction and revenue


##  Conclusion

The project successfully demonstrates how **K-Means clustering** can be used to segment customers based on purchasing behavior.
It provides meaningful insights through visualization and serves as a practical example of unsupervised machine learning.



