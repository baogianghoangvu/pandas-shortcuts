from pandas import DataFrame as D, Series as S

# Reindexing / selection / label manipulation

D.f2 = D.rename

## Heads or tails
D.h = D.head
S.h = S.head

D.t = D.tail
S.t = S.tail


## Duplicates
D.dd = D.drop_duplicates
S.dd = S.drop_duplicates

D.dup = D.duplicated
S.dup = S.duplicated


## Index
D.sx = D.set_index

D.rx = D.reset_index
S.rx = S.reset_index


# Reshaping, Sorting, Transposing

## Sort
D.si = D.sort_index
S.si = S.sort_index

D.sv = D.sort_values
S.sv = S.sort_values


## Pivot
D.pv = D.pivot

D.pvt = D.pivot_table


# Groupby
D.gb = D.groupby
S.gb = S.groupby


# Missing data handling
D.dna = D.dropna
S.dna = S.dropna

D.fna = D.fillna
S.fna = S.fillna


# Computations / descriptive stats
D.desc = D.describe

D.vc = D.cv = D.value_counts
S.vc = S.cv = S.value_counts

D.nu = D.nunique
S.nu = S.nunique

S.u = S.unique


# Properties
D.c = D.columns

D.i = D.index
S.i = S.index


# IO
D.cb = D.to_clipboard
S.cb = S.to_clipboard

D.dict = D.to_dict
S.dict = S.to_dict

S.list = S.to_list

D.np = D.to_numpy
S.np = S.to_numpy

## File types
D.csv = D.to_csv
S.csv = S.to_csv

D.html = D.to_html

D.json = D.to_json
S.json = S.to_json

D.md = D.to_markdown
S.md = S.to_markdown

D.parquet = D.to_parquet

D.xlsx = D.to_excel
S.xlsx = S.to_excel
