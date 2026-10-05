USE supply_chain_intelligence;

-- Executive KPIs
SELECT COUNT(DISTINCT order_id) AS distinct_orders,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit,
       SUM(profit)/NULLIF(SUM(sales),0)*100 AS profit_margin_pct,
       AVG(sla_breach)*100 AS sla_breach_pct,
       AVG(delivery_delay_days) AS avg_delivery_delay
FROM clean_orders;

-- Regional performance
SELECT region, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales,
       SUM(profit) AS profit, AVG(sla_breach)*100 AS sla_breach_pct
FROM clean_orders GROUP BY region ORDER BY profit DESC;

-- Shipping mode diagnostic
SELECT shipping_mode, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales,
       SUM(profit) AS profit, AVG(delivery_delay_days) AS avg_delay,
       AVG(sla_breach)*100 AS sla_breach_pct
FROM clean_orders GROUP BY shipping_mode ORDER BY sla_breach_pct DESC;

-- Category profitability
SELECT category_name, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales,
       SUM(profit) AS profit, SUM(profit)/NULLIF(SUM(sales),0)*100 AS margin_pct
FROM clean_orders GROUP BY category_name ORDER BY profit DESC;

-- Monthly trend
SELECT month, COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales,
       SUM(profit) AS profit, AVG(sla_breach)*100 AS sla_breach_pct
FROM clean_orders GROUP BY month ORDER BY month;

-- High-risk combinations: operational investigation candidates
SELECT region, shipping_mode, category_name,
       COUNT(DISTINCT order_id) AS orders, SUM(sales) AS sales,
       SUM(profit) AS profit, AVG(sla_breach)*100 AS sla_breach_pct
FROM clean_orders
GROUP BY region, shipping_mode, category_name
HAVING COUNT(DISTINCT order_id) >= 100
ORDER BY sla_breach_pct DESC, sales DESC;
