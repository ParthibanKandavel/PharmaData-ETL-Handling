
import pandas as pd
import sqlite3

# Load data
prescribers = pd.read_csv('../data/prescribers.csv')
rx_data = pd.read_csv('../data/rx_activity.csv')
call_logs = pd.read_csv('../data/veeva_calls.csv')

# Simple transformation
rx_summary = rx_data.groupby(['prescriber_id', 'drug_name']).agg({'quantity':'sum'}).reset_index()

# Join with prescriber details
merged = pd.merge(rx_summary, prescribers, on='prescriber_id', how='left')

# Save to SQLite (simulate Snowflake loading)
conn = sqlite3.connect('../data/pharma_dw.db')
merged.to_sql('rx_summary', conn, if_exists='replace', index=False)
conn.close()
