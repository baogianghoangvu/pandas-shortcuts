# pandas-shortcuts

[![.](https://img.shields.io/static/v1?logo=github&label=maintainer&message=baogianghoangvu&color=violet)](https://github.com/baogianghoangvu)

[![.](https://img.shields.io/badge/version-0.1-informational)](https://github.com/baogianghoangvu/pandas-shortcuts/blob/main/pandas_shortcuts/__init__.py)
[![.](https://img.shields.io/badge/python-3.6-important)](https://github.com/python/cpython)
[![.](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

Why even wait for autocompletion when you can use `pandas_shortcuts`?

## How to use

- Simply import `pandas_shortcuts` together with `pandas`.

  ```Python
  import pandas as pd
  import pandas_shortcuts
  ```

- Every `pd.DataFrame` and `pd.Series` objects will have:

  - shortcuts (full list [below](#available-shortcuts-and-methods))

  ```Python
  # shortcut for `df.head()`
  df.h()

  # shortcut for df.columns
  df.c

  # shortcut for df["col"].unique()
  df["col"].u()
  ```

  - new methods (full list [below](#available-shortcuts-and-methods))

  ```Python
  # view up to `r` rows and `c` columns of a dataframe, overiding pandas' default limit
  df.v()  # default r=50, c=50

  # view up to `r` rows of a series, overiding pandas' default limit
  df["col"].v(100)

  # stylize a dataframe's numeric columns as heatmap or bars
  # view up to `r` rows and `c` of a dataframe, overiding pandas' default limit
  df.sh()  # style=heatmap
  df.sb()  # style=bar

  # call `dtale.show`, refer to dtale docs for details
  df.dt()

  # call `pandas_profiling.ProfileReport`, refer to pandas_profiling docs for details
  df.pp()
  ```

## Available Shortcuts and Methods

```Python

# Heads or tails
df.h(...)  # df.head(...)
df.t(...)  # df.tail(...)
df["col"].h(...)  # df["col"].head(...)
df["col"].t(...)  # df["col"].tail(...)

# Sort
df.si(...)  # df.sort_index(...)
df["col"].si(...)  # df["col"].sort_index(...)
df.sv(...)  # df.sort_values(...)
df["col"].sv(...)  # df["col"].sort_values(...)

# Index
df.sx(...)  # df.set_index(...)
df.rx(...)  # df.reset_index(...)
df["col"].rx(...)  # df["col"].reset_index(...)

# Groupby
df.gb(...)  # df.groupby(...)
df["col"].gb(...)  # df["col"].groupby(...)

# Duplicates
df.dd(...)  # df.drop_duplicates(...)
df["col"].dd(...)  # df["col"].drop_duplicates(...)
df.dup(...)  # df.duplicated(...)
df["col"].dup(...)  # df["col"].duplicated(...)
df["col"].u(...)  # df["col"].unique(...)

# Properties
df.c  # df.columns
df.i  # df.index
df["col"].i  # df["col"].index


# Methods
df.v(...)
df["col"].v(...)
df.sh(...)
df.sb(...)
df.dt(...)
df.pp(...)
```

## Note

- `df.v()` directly generates `IPython.core.display.HTML` object under the hood, thus completely bypassing any `pd.set_option("display.max_rows", ...)` and `pd.set_option("display.max_columns", ...)` that the user may have specified.
