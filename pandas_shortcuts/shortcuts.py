from pandas import DataFrame as D, Series as S


# Heads or tails
D.h = D.head
D.t = D.tail
S.h = S.head
S.t = S.tail


# Index
D.sx = D.set_index
D.rx = D.reset_index
S.rx = S.reset_index


# Sort
D.si = D.sort_index
S.si = S.sort_index
D.sv = D.sort_values
S.sv = S.sort_values


# Groupby
D.gb = D.groupby
S.gb = S.groupby


# Duplicates
D.dd = D.drop_duplicates
S.dd = S.drop_duplicates
D.dup = D.duplicated
S.dup = S.duplicated
S.u = S.unique


# Properties
D.c = D.columns
D.i = D.index
S.i = S.index

