USE supply_chain_intelligence;

-- Run src/etl.py first to create data/processed/clean_orders.csv.
-- Replace the path below with your local absolute path.
LOAD DATA LOCAL INFILE 'data/processed/clean_orders.csv'
INTO TABLE clean_orders
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(order_id,order_item_id,customer_id,order_date,shipping_date,shipping_mode,market,region,country,state,city,customer_segment,category_name,department_name,product_name,order_status,actual_shipping_days,scheduled_shipping_days,late_delivery_risk,sales,profit,order_item_total,quantity,discount,product_price,delivery_delay_days,sla_breach,profit_margin_pct,month,year,quarter);
