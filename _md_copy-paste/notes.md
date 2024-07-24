## Note

- `df.v()` directly generates `IPython.core.display.HTML` object under the hood, thus completely bypassing any `pd.set_option("display.max_rows", ...)` and `pd.set_option("display.max_columns", ...)` that the user may have specified.