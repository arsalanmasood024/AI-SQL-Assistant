import io
import pandas as pd


def to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def to_excel(df):

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    output.seek(0)

    return output.getvalue()