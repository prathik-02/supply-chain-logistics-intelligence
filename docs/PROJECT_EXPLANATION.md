# Detailed Project Explanation

## 1. Project objective
Built an end-to-end supply-chain analytics solution to convert transactional order-item data into business KPIs, diagnostic SQL analysis, an interactive Power BI dashboard and a Streamlit analytics application.

## 2. Dataset understanding
The DataCo dataset contains 180,519 order-item records. Multiple rows can belong to the same order, so the project distinguishes between order-item volume and unique-order volume.

## 3. Data cleaning
- Selected analytical columns relevant to orders, delivery, geography, product category, sales and profit.
- Converted order/shipping dates into datetime values.
- Converted numerical business fields into numeric types.
- Removed rows missing essential order/date/financial fields.
- Removed duplicate order-item IDs.
- Excluded unnecessary customer/contact/product metadata from the analytical layer.

## 4. Feature engineering
- `delivery_delay_days = actual_shipping_days - scheduled_shipping_days`
- `sla_breach = 1` when actual delivery exceeded scheduled delivery days.
- `profit_margin_pct = profit / sales × 100`
- Derived month, year and quarter for trend analysis.

## 5. SQL analytics
Created queries for:
- Executive KPI reporting
- Regional performance
- Shipping-mode performance
- Category profitability
- Monthly sales/profit trends
- High-risk operational combinations
- Interview-style aggregation and ranking problems

## 6. Power BI
The model uses the order-item fact table with a Date dimension. DAX measures use `DISTINCTCOUNT(order_id)` for order-level KPIs. Dashboard pages cover executive performance, delivery operations, profitability and market/category analysis.

## 7. Streamlit
Built an interactive dashboard with filters for market, region and shipping mode. It displays monthly trends, regional profitability, shipping-mode SLA performance, market performance, category profitability and operational hotspots.

## 8. Business insights
- The business generated approximately $36.78M in sales and $3.97M in profit.
- Overall margin was about 10.79%.
- The observed SLA breach rate was 57.28%, making delivery performance a major diagnostic area.
- First Class shows a 100% observed SLA-breach rate in this dataset, while Standard Class is about 39.8%; this is an observation for investigation, not a causal conclusion.
- Approximately 18.71% of order-item records are negative-profit, suggesting opportunities to investigate discounts, freight, pricing and product economics.

## 9. Business value
The project gives a decision-maker one place to compare revenue, profit and operational service quality instead of looking only at sales. It also creates a repeatable ETL → SQL → BI → web-dashboard workflow.

## 10. Interview explanation
I treated the data as an order-item fact table and explicitly avoided using row count as order count. I cleaned the transactional data in Python, engineered delivery and profitability metrics, loaded the analytical layer into MySQL, built reusable SQL queries and DAX measures, and then exposed the results through Power BI and Streamlit. The main analytical focus was identifying where high volume, low profitability and poor delivery performance overlap.
