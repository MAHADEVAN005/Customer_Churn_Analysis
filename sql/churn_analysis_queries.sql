-- create database
create database churn_analysis;
use churn_analysis;

-- Analysis
SELECT Region,
       COUNT(*) AS Total,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned,
       ROUND((SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) AS ChurnPercentage
FROM Customer
GROUP BY Region
ORDER BY ChurnPercentage DESC;

SELECT SupportTickets,
       COUNT(*) AS TotalCustomers,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned
FROM Customer
GROUP BY SupportTickets
ORDER BY SupportTickets DESC;

SELECT MonthlyCharges,
       COUNT(*) AS Total,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned
FROM Customer
GROUP BY MonthlyCharges
ORDER BY Churned DESC
LIMIT 10;

SELECT *
FROM Customer
WHERE Tenure < 6 AND Churn = 'Yes';

SELECT CustomerSatisfaction,
       COUNT(*) AS Total,
       SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned
FROM Customer
GROUP BY CustomerSatisfaction
ORDER BY CustomerSatisfaction ASC;

SELECT CustomerID, Age, Tenure, SupportTickets, MonthlyCharges, CustomerSatisfaction
FROM Customer
WHERE (Tenure < 6 OR CustomerSatisfaction <= 2 OR SupportTickets >= 4)
  AND Churn = 'Yes';
