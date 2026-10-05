# Project 1 — What to do on your PC

## Step 1 — MySQL
1. Install MySQL 8.x and MySQL Workbench.
2. Open `sql/01_schema.sql` and run it.
3. Put `data/processed/clean_orders.csv` somewhere easy to find.
4. Open `sql/03_load_clean_orders.sql`.
5. Replace `C:/path/to/clean_orders.csv` with the actual Windows path.
6. Run the LOAD DATA command.
7. If MySQL reports that LOCAL INFILE is disabled, enable local loading for your MySQL client/server and rerun. MySQL documents `LOAD DATA LOCAL INFILE` as the bulk-loading method for local text files.
8. Run `sql/02_analysis_queries.sql` and `sql/04_interview_queries.sql`.

## Step 2 — Power BI
1. Open Power BI Desktop.
2. Import `data/processed/clean_orders.csv`.
3. Follow `powerbi/POWER_BI_BUILD_GUIDE.md`.
4. Create the DateTable and DAX measures.
5. Build the four report pages.
6. Save as `Supply_Chain_Intelligence.pbix`.

## Step 3 — GitHub
Recommended repository name:
`data-analyst-supply-chain-intelligence`

Recommended top-level structure:
- data/processed/
- sql/
- powerbi/
- reports/
- README.md

Do NOT commit personal/customer PII or passwords from the original raw dataset.
