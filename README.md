📉 Customer Churn Analysis (Python + SQL)

A complete end-to-end customer churn analysis project using
SQL, Python (Pandas, NumPy, Matplotlib), and a synthetic dataset (1000 records).
This project analyzes customer behavior, churn patterns, and service usage impact to identify key factors that lead to customer churn and provides improvement strategies to retain customers.

📁 Project Structure
Customer-Churn-Analysis/
├── data/
│   └── customer_churn_dataset_1000.csv
├── analysis/
│   └── churn_analysis.ipynb or churn_analysis.py
├── sql/
│   └── churn_analysis_queries.sql
├── visuals/
│   ├── churn_count.png
│   ├── monthly_charges_vs_churn.png
│   └── support_tickets_vs_churn.png
└── README.md

💡 Overview

This project focuses on:

Data Cleaning

Exploratory Data Analysis (EDA)

Customer Segmentation

Churn Pattern Identification

Visualization

Business Recommendations

Tools Used:

MySQL (Structural Queries)

Python (Pandas, NumPy, Matplotlib)

Excel (Optional report / dashboard)

🗂 Dataset Info

The dataset contains:

1000 customer records

Key Features:

CustomerID

Age

Tenure

MonthlyCharges

InternetUsageGB

SupportTickets

Satisfaction Score

Region

Churn (Yes/No)

Dataset was generated to represent telecom/internet service provider customer behavior, similar to JioFiber / Airtel Broadband users.

🔍 SQL Analysis Performed
✔ Total Customers & Churn Rate
✔ Churned vs Retained Customers
✔ Region-wise Churn
✔ Tenure Categorization
✔ High-risk Customers Identification
✔ Data Import & Validation

SQL was mainly used to understand data structure and extract churn metrics.

🐍 Python Analysis (Main Part)

Using Pandas + Matplotlib, the following were done:

✔ Data Cleaning

Checked missing values

Converted numerical data types

Verified categorical balance

✔ KPI Analysis

Total Customers

Churn Percentage

Average Tenure

Average Monthly Charges

Avg Support Tickets per segment

✔ Detailed Analysis

Monthly Charges vs Churn

Support Tickets vs Churn

Tenure-based retention

Satisfaction impact (optional)

Identification of high-risk churn customers

📊 Visualizations Included
📌 Churn Count (Bar Chart)

Shows majority retained & minority churned customers.

📌 Monthly Charges vs Churn (Box Plot)

Indicates churned customers tend to have higher billing.

📌 Support Tickets vs Churn (Box Plot)

Shows customers with more complaints are more likely to churn.

🧠 Final Business Insights
1. ⭐ High Monthly Charges

Customers with higher subscription fees show higher churn probability.

2. ⭐ Poor Customer Support

More support tickets = more churn. Frequent complaints drive customer drop-off.

3. ⭐ Short-Service Users Leave Early

Customers with low tenure (< 6 months) tend to churn early.

4. ⭐ Customer Satisfaction

Lower satisfaction ratings strongly correlate with churn (trend observed).

5. ⭐ Retention Strategy Needed

High-paying but dissatisfied customers are most at-risk.

🏁 Conclusion

This project demonstrates:

SQL-based data validation

Python-based detailed churn analytics

Visualization-driven insights

Real-time business-oriented analysis

Understanding of churn risk factors

It is suitable for:

📊 Data Analyst Portfolio

🎓 Academic Project

🧪 Interview Showcase

💼 GitHub Projects

🚀 Future Enhancements

Implement Churn Prediction Model (Logistic Regression / Random Forest)

Develop Customer Risk Scoring System

Build Dashboard using Power BI or Tableau

Add Automated Alerts for high-risk customers

🙌 Acknowledgements

Dataset generated manually for learning and analytics demonstration purposes.
