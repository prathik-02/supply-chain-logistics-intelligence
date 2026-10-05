# Supply Chain & Logistics Intelligence Dashboard

An end-to-end Data Analyst portfolio project using the **DataCo Smart Supply Chain** dataset to analyze sales, profitability, delivery performance and operational hotspots.

## Business problem
A supply-chain organization needs to answer:
- Which markets, regions and categories generate the most revenue and profit?
- Where are delivery/SLA problems concentrated?
- How do shipping modes differ in operational performance?
- Which business areas deserve investigation based on the combination of volume, profitability and delivery performance?

## Key results from the supplied dataset
- **65,752 distinct orders** across **180,519 order-item records**.
- **$36.78M sales** and **$3.97M profit**.
- Overall profit margin: **10.79%**.
- Observed SLA breach rate: **57.28%**.
- Average delivery delay versus scheduled days: **0.57 days**.
- About **18.71% of order-item records are negative-profit**, indicating meaningful profitability leakage worth investigating.

> Important: the source is at order-item grain. Order KPIs therefore use `DISTINCTCOUNT(order_id)` rather than row counts.

## Tech stack
- Python / Pandas — ETL, cleaning and KPI generation
- MySQL — relational storage and SQL analysis
- Power BI — interactive BI dashboard and DAX measures
- Streamlit — lightweight web analytics application
- Git/GitHub — version control and portfolio delivery

## Repository structure
```text
.
├── app/
│   └── streamlit_app.py
├── data/
│   ├── raw/                 # Put DataCoSupplyChainDataset.csv here locally
│   └── processed/           # Generated KPI CSVs; clean_orders.csv generated locally
├── docs/
│   ├── PROJECT_EXPLANATION.md
│   └── RESUME_AND_INTERVIEW.md
├── powerbi/
│   └── POWER_BI_BUILD_GUIDE.md
├── reports/
│   ├── executive_findings.md
│   └── key_business_findings.md
├── sql/
│   ├── 01_schema.sql
│   ├── 02_analysis_queries.sql
│   ├── 03_load_clean_orders.sql
│   └── 04_interview_queries.sql
├── src/
│   └── etl.py
├── requirements.txt
└── README.md
```

## Run locally
1. Create a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Put the supplied `DataCoSupplyChainDataset.csv` in `data/raw/`.
4. Run: `python src/etl.py --input data/raw/DataCoSupplyChainDataset.csv`
5. Launch: `streamlit run app/streamlit_app.py`

The Streamlit app can also run from a GitHub repository because it relies on the small processed KPI CSVs. Streamlit's official deployment flow uses a GitHub repository plus a `requirements.txt` file. citeturn0search0turn0search11

## MySQL
Create the database/table using `sql/01_schema.sql`, then load the generated `data/processed/clean_orders.csv` using `sql/03_load_clean_orders.sql`. Run the analysis queries in `sql/02_analysis_queries.sql`.

## Power BI
Follow `powerbi/POWER_BI_BUILD_GUIDE.md` for the model, DAX measures, page layout and visuals.

## Data governance
The raw DataCo file is intentionally not required in the GitHub repository. This keeps the repository lighter and avoids publishing raw customer-related fields. The ETL script reproduces the cleaned analytical layer from the raw source.

## Limitations
- This is descriptive/diagnostic analytics, not a production delivery-prediction system.
- `Late_delivery_risk`/SLA outcome fields should not be used as predictive inputs without a leakage-safe temporal design.
- The dataset is historical and anonymized; findings are portfolio analysis rather than current operational recommendations.
