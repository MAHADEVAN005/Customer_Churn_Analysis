import numpy as np
import pandas as pd

np.random.seed(18)
n=1000

data = {
    "CustomerID":[f"CUST{1000+i}"for i in range(n)],
    "Gender":np.random.choice(["Male","Female"],n),
    "Age":np.random.randint(18,60,n),
    "Tenure":np.random.randint(1,36,n),
    "SubscriptionType":np.random.choice(["Monthly","Yearly"],n),
    "MonthlyCharges":np.random.randint(500,3000,n),
    "TotalSpend":np.random.randint(1000,25000,n),
    "ContractPeriod":np.random.choice(["1 yr","2 yr","3 yr"],n),
    "SupportTickets":np.random.randint(0,7,n),
    "InternetUsageGB":np.random.uniform(50,300,n).round(2),
    "PaymentMode":np.random.choice(["Credit Card","UPI","NetBanking"],n),
    "Region":np.random.choice(["South","North","West","East"],n),
    "OffersUsed":np.random.randint(0,5,n),
    "LastInteractionDays":np.random.randint(1,30,n),
    "PartnerOrReferal":np.random.choice(["Yes","No"],n),
    "ActiveServiceCount":np.random.randint(1,5,n),
    "HasBackupPlan":np.random.choice(["Yes","No"],n),
    "CustomerSatisfaction":np.random.randint(1,6,n),
    "Churn":np.random.choice(["Yes","No"],n,p=[0.25,0.75])
}

df=pd.DataFrame(data)
df.to_csv("Customer_Churn_dataset.csv",index=False)
print("Dataset Created!!")