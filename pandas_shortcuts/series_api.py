from pandas import Series as S

# Reindexing / selection / label manipulation

## Heads or tails
S.h = S.head
S.t = S.tail

## Duplicates
S.dd = S.drop_duplicates
S.dup = S.duplicated

## Index
S.rx = S.reset_index

# Reshaping, Sorting, Transposing

## Sort
S.si = S.sort_index
S.sv = S.sort_values

# Groupby
S.gb = S.groupby

# Missing data handling
S.dna = S.dropna
S.fna = S.fillna

# Computations / descriptive stats
S.vc = S.cv = S.value_counts
S.nu = S.nunique
S.u = S.unique

# Properties
S.i = S.index

# IO
S.cb = S.to_clipboard
S.dict = S.to_dict
S.list = S.to_list
S.np = S.to_numpy

## File types
S.csv = S.to_csv
S.json = S.to_json
S.md = S.to_markdown
S.xlsx = S.to_excel
