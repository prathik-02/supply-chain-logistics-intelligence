USE supply_chain_intelligence;

-- Top 5 regions by profit
SELECT region, SUM(profit) AS profit FROM clean_orders GROUP BY region ORDER BY profit DESC LIMIT 5;

-- Categories with negative total profit
SELECT category_name, SUM(profit) AS profit FROM clean_orders GROUP BY category_name HAVING SUM(profit) < 0 ORDER BY profit;

-- Monthly profit margin
SELECT month, SUM(profit)/NULLIF(SUM(sales),0)*100 AS margin_pct
FROM clean_orders GROUP BY month ORDER BY month;

-- Customers/orders by segment
SELECT customer_segment, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales, SUM(profit) AS profit
FROM clean_orders GROUP BY customer_segment ORDER BY sales DESC;

-- Rank regions by profit using a window function
WITH r AS (
 SELECT region, SUM(profit) AS profit FROM clean_orders GROUP BY region
)
SELECT region, profit, DENSE_RANK() OVER (ORDER BY profit DESC) AS profit_rank FROM r;
