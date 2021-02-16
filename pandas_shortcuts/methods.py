import numpy as np
import pandas as pd
from dtale import show
from pandas import DataFrame as D
from pandas import Series as S
from pandas_profiling import ProfileReport

D.dt = show  # dtale.show
D.pp = ProfileReport  # pandas_profiling.ProfileReport


def _style_base(df, r=50, c=50, na_rep="-"):
    if r > len(df):
        _df = df.iloc[:, :c]
    else:
        _df = df.iloc[np.r_[0 : int(r / 2), -int(r / 2) : 0], :c]
    _df_numeric = _df.select_dtypes(include=np.number)
    column_format = {k: "{:0,.2f}" for k in _df_numeric.columns}
    return _df.style.format(column_format, na_rep=na_rep)


def style_heatmap(df, r=50, c=50, na_rep="-", colormap="YlOrRd"):
    base = _style_base(df, r=r, c=c, na_rep=na_rep)
    return base.background_gradient(cmap=colormap)


def style_bar(df, r=50, c=50, na_rep="-", width=50, bar_color="#d65f5f"):
    base = _style_base(df, r=r, c=c, na_rep=na_rep)
    return base.bar(color=bar_color, align="left", width=width)


D.sh = style_heatmap
D.sb = style_bar


try:
    from IPython.display import HTML

    def dataframe_view(df: pd.DataFrame, r=50, c=50) -> HTML:
        html = df.to_html(
            max_rows=r,
            max_cols=c,
            justify="left",
            show_dimensions=True,
        )
        return HTML(html)


except ModuleNotFoundError:

    def dataframe_view(df: pd.DataFrame, r=50, c=50) -> None:
        string = df.to_string(
            max_rows=r,
            max_cols=c,
            justify="left",
            show_dimensions=True,
        )
        return print(string)


def series_view(series: pd.Series, r=50) -> None:
    string = series.to_string(
        name=True,
        length=True,
        dtype=True,
        max_rows=r,
    )
    print(string)


D.v = dataframe_view
S.v = series_view
