import pandas as pd

pd.df = pd.DataFrame

# IO
pd.csv = pd.read_csv
pd.json = pd.read_json
pd.parquet = pd.read_parquet
pd.sql = pd.read_sql
pd.xlsx = pd.read_excel


# General function - Pivot
pd.pv = pd.pivot
pd.pvt = pd.pivot_table


# General function - datetime
pd.tdt = pd.to_datetime
pd.ttd = pd.to_timedelta
