import plotly.express as px


def auto_chart(df):

    if len(df.columns) < 2:
        return None

    x = df.columns[0]
    y = df.columns[1]

    if df[y].dtype == "object":
        return None

    fig = px.bar(
        df,
        x=x,
        y=y,
        text=y,
        title="Visualization"
    )

    fig.update_layout(height=500)

    return fig