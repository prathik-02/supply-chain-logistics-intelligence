# Resume & Interview Material

## Resume-ready project title
**Supply Chain & Logistics Intelligence Dashboard | Python, SQL, Power BI, Streamlit**

## Resume bullets
- Processed and analyzed **180K+ order-item records** using Python/Pandas; engineered delivery-delay, SLA-breach and profit-margin metrics while preserving correct order-level aggregation across **65K+ unique orders**.
- Built MySQL analytics and Power BI dashboards to track **$36.78M sales, $3.97M profit, 10.79% margin and 57.28% observed SLA breaches** across markets, regions, categories and shipping modes.
- Developed an interactive Streamlit dashboard with KPI cards, trend analysis, regional profitability, shipping performance and category diagnostics to identify operational and profitability hotspots.

## 30-second explanation
"I built an end-to-end supply-chain analytics project using the DataCo dataset. I cleaned the order-item data in Python, created delivery and profitability KPIs, used MySQL for business analysis, built a Power BI dashboard, and created a Streamlit web dashboard. A key part was handling the data correctly because 180K rows represent order items, not 180K unique orders. The analysis found $36.78M in sales, $3.97M in profit and a 57.28% observed SLA-breach rate, which helped identify delivery and profitability areas for investigation."

## Common interview questions
**Why did you use DISTINCTCOUNT for orders?**
Because multiple order-item rows can belong to the same order. Counting rows would overstate the number of orders.

**Why Python?**
For reproducible cleaning, feature engineering and automated generation of analytical tables.

**Why MySQL?**
To demonstrate relational data modeling, aggregation, filtering, grouping and business-oriented SQL analysis.

**Why Power BI and Streamlit?**
Power BI demonstrates professional BI/reporting skills; Streamlit demonstrates that the same analysis can be turned into a lightweight interactive application.

**What was the biggest data challenge?**
Correctly handling the dataset grain and incomplete/unnecessary fields while preventing misleading KPIs.

**What does SLA breach mean here?**
An order-item record where actual shipping/delivery days exceeded scheduled shipping days. It is treated as an observed operational outcome, not as a predictive feature.

**What would you improve next?**
Add a leakage-safe temporal model for predicting future delivery risk, connect the dashboard to a live warehouse, add automated data-quality checks, and implement scheduled refreshes.
