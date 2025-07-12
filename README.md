
# Pharma ETL Mock Project

This project simulates a pharmaceutical ETL data pipeline using IQVIA-like and Veeva-like datasets. The ETL is built using Python and demonstrates basic ingestion, transformation, and loading of sample pharma datasets.

## Key Components

- **Data**: Contains mock input CSV files representing prescriber data, prescription activity, and sales rep call logs.
- **ETL**: Python scripts to read, clean, and transform raw data.
- **SQL**: DDL scripts to create target star schema tables.
- **Notebooks**: For EDA and analysis in Jupyter notebooks.
- **Reports**: Power BI visuals exported as PDFs or PNGs.
- **Docs**: Project documentation and assumptions.

## Tools Used

- Python (pandas, sqlalchemy)
- Snowflake / SQLite (for simulation)
- Power BI (for visual analytics)
- Git (for version control)

## Use Cases Simulated

- Call plan adherence using Veeva CRM-like data.
- Prescription trend analysis using IQVIA-like LRx data.
- Territory-level sales KPI dashboarding.

## Folder Structure

```
pharma_etl_mock_project/
prescribers,rx_activity,veeva_calls.csv              # Raw sample data files (CSV)
pharma_etl_pipeline.py                               # Python scripts for ETL
create_tables.sql                                    # Schema and table creation script

---

This project is for learning and demonstration purposes only. Data used is fully synthetic.
