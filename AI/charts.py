import plotly.express as px


def create_chart(df):

    if df.empty:
        return None

    columns = list(df.columns)

    if len(columns) < 2:
        return None

    x = columns[0]
    y = columns[1]

    if "month" in x.lower():
        return px.line(df, x=x, y=y)

    if "date" in x.lower():
        return px.line(df, x=x, y=y)

    if "category" in x.lower():
        return px.bar(df, x=x, y=y)

    if "product" in x.lower():
        return px.bar(df, x=x, y=y)

    if "customer" in x.lower():
        return px.bar(df, x=x, y=y)

    return px.bar(df, x=x, y=y)