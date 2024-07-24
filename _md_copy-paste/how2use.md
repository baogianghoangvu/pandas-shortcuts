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