<h1 align="center">pandas-shortcuts</h1>

<p align="center">Why even wait for autocompletion when you can use <code>pandas_shortcuts</code>?
</p>

<p align="center">
<a href="https://github.com/baogianghoangvu"><img src="https://img.shields.io/static/v1?logo=github&label=maintainer&message=baogianghoangvu&color=violet"></a>
<a href="https://github.com/lpun-majessica"><img src="https://img.shields.io/static/v1?logo=github&label=co-maintainer&message=lpun-majessica&color=3EAAAF"></a>
</p>
<p align="center">
<a href="https://github.com/baogianghoangvu/pandas-shortcuts/blob/main/pandas_shortcuts/__init__.py"><img src="https://img.shields.io/badge/version-0.1-informational"></a>
<a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/python->=3.6-important"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black"></a>
</p>

## How to use

- Simply import `pandas_shortcuts` together with `pandas`.

  ```Python
  import pandas as pd
  import pandas_shortcuts
  ```

- Every `pd.DataFrame` and `pd.Series` objects will have:

  - Shortcuts (full list [below](#available-shortcuts-and-methods))

  ```Python
  # shortcut for `df.head()`
  df.h()

  # shortcut for df.columns
  df.c

  # shortcut for df["col"].unique()
  df["col"].u()
  ```

  - New methods (full list [below](#available-shortcuts-and-methods))

  ```Python
  # view up to `r` rows and `c` columns of a dataframe, overriding pandas' default limit
  df.v()  # default r=50, c=50

  # view up to `r` rows of a series, overriding pandas' default limit
  df["col"].v(100)

  # stylize a dataframe's numeric columns as heatmap or bars
  # view up to `r` rows and `c` of a dataframe, overriding pandas' default limit
  df.sh()  # style=heatmap
  df.sb()  # style=bar
  ```

## Note

- `df.v()` directly generates `IPython.core.display.HTML` object under the hood, thus completely bypassing any `pd.set_option("display.max_rows", ...)` and `pd.set_option("display.max_columns", ...)` that the user may have specified.

## Available Shortcuts and Methods

<details>
<summary><b><i><font size="3">
Top Level API
</font></i></b></summary>

```Python
pd.df # pd.DataFrame

# IO
pd.csv # pd.read_csv
pd.json # pd.read_json
pd.parquet # pd.read_parquet
pd.sql # pd.read_sql
pd.xlsx # pd.read_excel


# General function - Pivot
pd.pv # pd.pivot
pd.pvt # pd.pivot_table


# General function - datetime
pd.tdt # pd.to_datetime
pd.ttd # pd.to_timedelta
```
</details>

<details>
<summary><b><i><font size="3">
Dataframe API
</font></i></b></summary>

```Python
# Reindexing / selection / label manipulation

df.f2 # df.rename

## Heads or tails
df.h # df.head
df.t # df.tail

## Duplicates
df.dd # df.drop_duplicates
df.dup # df.duplicated

## Index
df.sx # df.set_index
df.rx # df.reset_index

# Reshaping, Sorting, Transposing

## Sort
df.si # df.sort_index
df.sv # df.sort_values

## Pivot
df.pv # df.pivot
df.pvt # df.pivot_table

# Groupby
df.gb # df.groupby

# Missing data handling
df.dna # df.dropna
df.fna # df.fillna

# Computations / descriptive stats
df.desc # df.describe
df.vc # df.cv # df.value_counts
df.nu # df.nunique

# Properties
df.c # df.columns
df.i # df.index

# IO
df.cb # df.to_clipboard
df.dict # df.to_dict
df.np # df.to_numpy

## File types
df.csv # df.to_csv
df.html # df.to_html
df.json # df.to_json
df.md # df.to_markdown
df.parquet # df.to_parquet
df.xlsx # df.to_excel
```
</details>

<details>
<summary><b><i><font size="3">
Series API
</font></i></b></summary>

```Python
# Reindexing / selection / label manipulation

## Heads or tails
df["col"].h # df["col"].head
df["col"].t # df["col"].tail

## Duplicates
df["col"].dd # df["col"].drop_duplicates
df["col"].dup # df["col"].duplicated

## Index
df["col"].rx # df["col"].reset_index

# Reshaping, Sorting, Transposing

## Sort
df["col"].si # df["col"].sort_index
df["col"].sv # df["col"].sort_values

# Groupby
df["col"].gb # df["col"].groupby

# Missing data handling
df["col"].dna # df["col"].dropna
df["col"].fna # df["col"].fillna

# Computations / descriptive stats
df["col"].vc # df["col"].cv # df["col"].value_counts
df["col"].nu # df["col"].nunique
df["col"].u # df["col"].unique

# Properties
df["col"].i # df["col"].index

# IO
df["col"].cb # df["col"].to_clipboard
df["col"].dict # df["col"].to_dict
df["col"].list # df["col"].to_list
df["col"].np # df["col"].to_numpy

## File types
df["col"].csv # df["col"].to_csv
df["col"].json # df["col"].to_json
df["col"].md # df["col"].to_markdown
df["col"].xlsx # df["col"].to_excel
```
</details>

<details>
<summary><b><i><font size="3">
Methods
</font></i></b></summary>

```Python
df.sh # style_heatmap
df.sb # style_bar
df.v # dataframe_view
df["col"].v # series_view
```
</details>

