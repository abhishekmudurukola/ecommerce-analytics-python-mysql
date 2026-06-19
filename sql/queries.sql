USE ecommerce_analytics;

SELECT ROUND(SUM(Sales),2) AS Total_Sales
FROM superstore;

SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM superstore;

SELECT Category,
       ROUND(SUM(Sales),2) AS Sales
FROM superstore
GROUP BY Category
ORDER BY Sales DESC;

SELECT Region,
       ROUND(SUM(Sales),2) AS Sales
FROM superstore
GROUP BY Region
ORDER BY Sales DESC;

SELECT State,
       ROUND(SUM(Sales),2) AS Sales
FROM superstore
GROUP BY State
ORDER BY Sales DESC
LIMIT 10;