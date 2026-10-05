"""DataCo Smart Supply Chain ETL and KPI generation.

Usage:
    python src/etl.py --input data/raw/DataCoSupplyChainDataset.csv
"""
import argparse
from pathlib import Path
import pandas as pd

KEEP = {
    'Order Id':'order_id', 'Order Item Id':'order_item_id', 'Order Customer Id':'customer_id',
    'order date (DateOrders)':'order_date', 'Shipping Date (DateOrders)':'shipping_date',
    'Shipping Mode':'shipping_mode', 'Market':'market', 'Order Region':'region',
    'Order Country':'country', 'Order State':'state', 'Order City':'city',
    'Customer Segment':'customer_segment', 'Category Name':'category_name',
    'Department Name':'department_name', 'Product Name':'product_name',
    'Order Status':'order_status', 'Days for shipping (real)':'actual_shipping_days',
    'Days for shipment (scheduled)':'scheduled_shipping_days', 'Late_delivery_risk':'late_delivery_risk',
    'Sales':'sales', 'Order Profit Per Order':'profit', 'Order Item Total':'order_item_total',
    'Order Item Quantity':'quantity', 'Order Item Discount':'discount', 'Product Price':'product_price'
}

def run(input_file: str, output_dir: str = 'data/processed'):
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_file, encoding='latin1')
    required = [c for c in KEEP if c != 'Shipping Date (DateOrders)']
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Missing expected columns: {missing}')
    if 'Shipping Date (DateOrders)' not in df.columns:
        df['Shipping Date (DateOrders)'] = pd.NaT
    df = df[list(KEEP)].rename(columns=KEEP)
    for c in ['order_date','shipping_date']:
        df[c] = pd.to_datetime(df[c], errors='coerce')
    numeric = ['actual_shipping_days','scheduled_shipping_days','late_delivery_risk','sales','profit','order_item_total','quantity','discount','product_price']
    for c in numeric:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['delivery_delay_days'] = df['actual_shipping_days'] - df['scheduled_shipping_days']
    df['sla_breach'] = (df['delivery_delay_days'] > 0).astype(int)
    df['profit_margin_pct'] = (df['profit'] / df['sales'].replace(0, pd.NA) * 100).round(4)
    df['month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    df['year'] = df['order_date'].dt.year
    df['quarter'] = df['order_date'].dt.to_period('Q').astype(str)
    df = df.dropna(subset=['order_id','order_date','sales','profit']).drop_duplicates(subset=['order_item_id'])
    df.to_csv(out/'clean_orders.csv', index=False)

    def kpi(group_cols):
        g = df.groupby(group_cols, dropna=False)
        r = g.agg(order_items=('order_item_id','nunique'), orders=('order_id','nunique'), sales=('sales','sum'), profit=('profit','sum'), avg_delay=('delivery_delay_days','mean'), sla_breach_pct=('sla_breach','mean')).reset_index()
        r['sla_breach_pct'] *= 100
        r['profit_margin_pct'] = r['profit'] / r['sales'].replace(0, pd.NA) * 100
        return r.round(4)
    kpi(['market']).to_csv(out/'market_kpis.csv', index=False)
    kpi(['region']).to_csv(out/'region_kpis.csv', index=False)
    kpi(['category_name']).to_csv(out/'category_kpis.csv', index=False)
    kpi(['shipping_mode']).to_csv(out/'shipping_kpis.csv', index=False)
    kpi(['month']).to_csv(out/'monthly_kpis.csv', index=False)
    print(f'Rows after cleaning: {len(df):,}')
    print(f'Distinct orders: {df.order_id.nunique():,}')
    print(f'Sales: ${df.sales.sum():,.2f}')
    print(f'Profit: ${df.profit.sum():,.2f}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', default='data/raw/DataCoSupplyChainDataset.csv')
    ap.add_argument('--output', default='data/processed')
    args = ap.parse_args()
    run(args.input, args.output)
