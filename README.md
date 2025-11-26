# 📊 Customer Churn Analysis

This project performs churn analysis on a simulated internet service provider dataset (like Jio Fiber / Airtel Broadband). It identifies key reasons why customers stop using the service.

## 🔍 Project Objective
To analyze customer behavior and identify factors contributing to churn using Python and SQL, and to provide business insights to improve customer retention.

---

## 🛠️ Tools & Technologies
| Category | Tools |
|----------|-------|
| Programming | Python (pandas, NumPy, matplotlib) |
| Database | MySQL / SQL |
| Analysis | VISUAL STUDIO |
| Dataset | CSV (1000 records) |

---

## 📎 Dataset Details
- **1000 customer records**
- Includes fields like:
  - MonthlyCharges, Tenure, SupportTickets, InternetUsageGB  
  - CustomerSatisfaction, Region, Churn (Yes/No)

---

## 📈 Key Insights
✔ Customers with **high monthly charges** have higher churn risk  
✔ Churn rate is highest for **tenure < 6 months** (new users)  
✔ **Support complaints (tickets > 3)** strongly lead to churn  
✔ **Low customer satisfaction (<= 2)** is a major churn indicator  

---

## 🗂 Folder Structure

Customer-Churn-Analysis/
├── data/
├── analysis/
├── sql/
├── visuals/
└── README.md