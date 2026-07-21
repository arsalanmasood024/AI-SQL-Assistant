import pandas as pd
import plotly.express as px


def auto_chart(df):

    if df.empty:
        return None

    if len(df.columns) < 2:
        return None

    x = df.columns[0]
    y = df.columns[1]

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        return None

    y = numeric_cols[0]

    x_lower = x.lower()

    # Monthly Trend
    if "month" in x_lower or "date" in x_lower:

        fig = px.line(
            df,
            x=x,
            y=y,
            markers=True,
            title="Trend Analysis"
        )

        return fig

    # Pie Chart
    if any(word in x_lower for word in [
        "status",
        "category",
        "department"
    ]):

        fig = px.pie(
            df,
            names=x,
            values=y,
            title="Distribution"
        )

        return fig

    # Horizontal Bar
    if len(df) <= 15:

        fig = px.bar(
            df,
            x=y,
            y=x,
            orientation="h",
            text=y,
            title="Analysis"
        )

        fig.update_layout(
            yaxis={"categoryorder": "total ascending"}
        )

        return fig

    # Default Bar
    fig = px.bar(
        df,
        x=x,
        y=y,
        text=y,
        title="Analysis"
    )

    return fig