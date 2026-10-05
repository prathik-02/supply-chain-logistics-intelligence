import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'processed'

st.set_page_config(page_title='Supply Chain Intelligence', page_icon='📦', layout='wide')
st.title('📦 Supply Chain & Logistics Intelligence')
st.caption('DataCo Smart Supply Chain | Operational, delivery and profitability analytics')

@st.cache_data
def load(name):
    return pd.read_csv(DATA / name)

market = load('market_kpis.csv')
region = load('region_kpis.csv')
category = load('category_kpis.csv')
shipping = load('shipping_kpis.csv')
monthly = load('monthly_kpis.csv')

st.sidebar.header('Dashboard Filters')
markets = st.sidebar.multiselect('Market', sorted(market.market.dropna().unique()), default=sorted(market.market.dropna().unique()))
regions = st.sidebar.multiselect('Region', sorted(region.region.dropna().unique()), default=sorted(region.region.dropna().unique()))
shipping_modes = st.sidebar.multiselect('Shipping Mode', sorted(shipping.shipping_mode.dropna().unique()), default=sorted(shipping.shipping_mode.dropna().unique()))

# Dataset-level KPIs from the actual project analysis.
orders, sales, profit, margin, sla, delay = 65752, 36784735.01, 3966902.97, 10.79, 57.28, 0.57
c = st.columns(6)
for col, label, value in zip(c, ['Distinct Orders','Sales','Profit','Profit Margin','SLA Breach Rate','Avg Delivery Delay'], [f'{orders:,}',f'${sales/1e6:.2f}M',f'${profit/1e6:.2f}M',f'{margin:.2f}%',f'{sla:.2f}%',f'{delay:.2f} days']):
    col.metric(label, value)

reg = region[region.region.isin(regions)].sort_values('profit', ascending=False)
ship = shipping[shipping.shipping_mode.isin(shipping_modes)].sort_values('sla_breach_pct', ascending=False)
mar = market[market.market.isin(markets)]

st.divider()
a,b = st.columns(2)
with a:
    st.subheader('Monthly Sales & Profit')
    m = monthly.copy(); m['month'] = pd.to_datetime(m['month']); m = m.sort_values('month').set_index('month')
    st.line_chart(m[['sales','profit']])
with b:
    st.subheader('Profit by Region')
    st.bar_chart(reg.set_index('region')['profit'])

a,b = st.columns(2)
with a:
    st.subheader('SLA Breach by Shipping Mode')
    st.bar_chart(ship.set_index('shipping_mode')['sla_breach_pct'])
with b:
    st.subheader('Market Performance')
    st.dataframe(mar[['market','orders','sales','profit','sla_breach_pct','profit_margin_pct']].sort_values('sales', ascending=False), use_container_width=True, hide_index=True)

st.subheader('Category Profitability')
st.dataframe(category[['category_name','orders','sales','profit','profit_margin_pct','sla_breach_pct']].sort_values('sales', ascending=False), use_container_width=True, hide_index=True)

st.subheader('Operational Hotspots')
st.dataframe(ship[['shipping_mode','orders','sales','profit','avg_delay','sla_breach_pct','profit_margin_pct']], use_container_width=True, hide_index=True)

st.info('Interpretation: SLA breach is a descriptive outcome metric. It is not treated as a pre-delivery prediction feature in this project.')
