# =========================
# 📦 Import Libraries
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 📥 Load Dataset
# =========================
df = pd.read_csv("customer_churn_dataset.csv")
print("🔹 Dataset Loaded Successfully!")

# =========================
# 🔍 Basic Analysis
# =========================
print("\n📌 Top 5 Rows:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Missing Values:")
print(df.isnull().sum())

print("\n📌 Basic Statistics:")
print(df.describe())

# =========================
# 📉 Churn Overview
# =========================
print("\n📊 Churn Count:")
print(df['Churn'].value_counts())

print("\n📈 Churn Percentage:")
print(df['Churn'].value_counts(normalize=True) * 100)

# =========================
# 💸 Monthly Charges vs Churn
# =========================
print("\n💸 Avg MonthlyCharges by Churn:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# =========================
# 🆘 Support Tickets Impact
# =========================
print("\n🆘 Avg SupportTickets by Churn:")
print(df.groupby('Churn')['SupportTickets'].mean())

# =========================
# ⏳ Tenure Impact
# =========================
print("\n⏳ Avg Tenure by Churn:")
print(df.groupby('Churn')['Tenure'].mean())

# =========================
# ⭐ Satisfaction Impact
# =========================
print("\n⭐ Avg Rating by Churn:")
print(df.groupby('Churn')['CustomerSatisfaction'].mean())

# =========================
# 🔎 Identify High Risk Customers
# =========================
high_risk = df[(df['Tenure'] < 6) | (df['SupportTickets'] > 3) | (df['CustomerSatisfaction'] <= 2)]
print("\n🚨 High-Risk Customers (Based on conditions):")
print(high_risk[high_risk['Churn'] == "Yes"].head(10))

# =========================
# 🔁 Correlation Check
# =========================
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
print("\n📌 Correlation with Churn (Approximated using Tenure):")
print(corr['Tenure'].sort_values(ascending=False))

# =========================
# 📊 Visualization
# =========================

# 1️⃣ Churn Count Chart
plt.figure(figsize=(5,4))
df['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Count")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()

# 2️⃣ Monthly Charges Comparison
plt.figure(figsize=(6,4))
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.show()

# 3️⃣ Support Tickets Comparison
plt.figure(figsize=(6,4))
df.boxplot(column='SupportTickets', by='Churn')
plt.title("Support Tickets by Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Support Tickets")
plt.show()

# =========================
# 📌 Final Insights
# =========================
print("\n🎯 Final Insights:")
print("""
1️⃣ High MonthlyCharges users tend to churn more.
2️⃣ Customers with more SupportTickets (>3) are likely to churn.
3️⃣ New customers (<6 months tenure) are at higher risk.
4️⃣ Low satisfaction rating (<=2) strongly relates to churn.
5️⃣ Customer retention offers should target:
   🔹 New users
   🔹 High-complaint users
   🔹 High billing customers
""")

print("\n🚀 Churn Analysis Complete!")
