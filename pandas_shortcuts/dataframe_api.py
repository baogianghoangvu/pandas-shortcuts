from pandas import DataFrame as D

# Reindexing / selection / label manipulation

D.f2 = D.rename

## Heads or tails
D.h = D.head
D.t = D.tail

## Duplicates
D.dd = D.drop_duplicates
D.dup = D.duplicated

## Index
D.sx = D.set_index
D.rx = D.reset_index

# Reshaping, Sorting, Transposing

## Sort
D.si = D.sort_index
D.sv = D.sort_values

## Pivot
D.pv = D.pivot
D.pvt = D.pivot_table

# Groupby
D.gb = D.groupby

# Missing data handling
D.dna = D.dropna
D.fna = D.fillna

# Computations / descriptive stats
D.desc = D.describe
D.vc = D.cv = D.value_counts
D.nu = D.nunique

# Properties
D.c = D.columns
D.i = D.index

# IO
D.cb = D.to_clipboard
D.dict = D.to_dict
D.np = D.to_numpy

## File types
D.csv = D.to_csv
D.html = D.to_html
D.json = D.to_json
D.md = D.to_markdown
D.parquet = D.to_parquet
D.xlsx = D.to_excel
