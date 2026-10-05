# Supply Chain Intelligence — DataCo Results

## Dataset
- Raw records: 180,519
- Distinct orders: 65,752
- Distinct order items: 180,519
- Date range: 2015-01-01 to 2018-01-31

## Executive KPIs
- Sales: $36,784,735.01
- Profit: $3,966,902.97
- Profit margin: 10.78%
- Average delivery delay vs scheduled: 0.57 days
- Late-delivery-risk flag at item level: 54.83%
- SLA breach based on actual minus scheduled shipping days: 57.28%
- Negative-profit order items: 18.71%

## Important grain / metric rule
The raw file is at order-item level. Therefore:
- Use DISTINCT Order Id for order counts.
- Use order-item rows for item-level operational analysis.
- Do not describe 180,519 rows as 180,519 orders.

## Data-quality decisions
- Removed direct customer PII fields from the analytical model.
- Excluded highly incomplete location fields where not needed.
- Excluded the 100%-missing Product Description from analysis.
- Preserved operational fields needed for descriptive delivery analysis.
- Added delivery_delay_days = actual shipping days - scheduled shipping days.
- Added sla_breach = delivery_delay_days > 0.
- Added month, year, quarter, and profit_margin_pct.

## Caution
Late_delivery_risk is an outcome flag, so it should be used for historical/descriptive delivery reporting rather than presented as an order-time prediction input. For a future predictive model, post-outcome fields such as actual shipping duration and delivery status must be excluded.
