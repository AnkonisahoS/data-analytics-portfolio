-- Retail Sales SQL analysis (SQLite-compatible)
-- 1. Revenue and profit overview
SELECT ROUND(SUM(Sales),2) AS total_sales, ROUND(SUM(Profit),2) AS total_profit,
       ROUND(AVG(Sales),2) AS avg_order_value FROM retail_sales;

-- 2. Sales by category
SELECT Category, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
FROM retail_sales GROUP BY Category ORDER BY sales DESC;

-- 3. Sales by region
SELECT Region, ROUND(SUM(Sales),2) AS sales FROM retail_sales
GROUP BY Region ORDER BY sales DESC;

-- 4. Monthly trend (SQLite)
SELECT strftime('%Y-%m', OrderDate) AS month, ROUND(SUM(Sales),2) AS sales
FROM retail_sales GROUP BY month ORDER BY month;

-- 5. Discount impact (descriptive)
SELECT Discount, COUNT(*) AS orders, ROUND(AVG(Sales),2) AS avg_sales,
       ROUND(AVG(Profit),2) AS avg_profit
FROM retail_sales GROUP BY Discount ORDER BY Discount;
