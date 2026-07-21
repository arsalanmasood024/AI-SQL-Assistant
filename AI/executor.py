import time
import pandas as pd
from database.connection import get_engine

engine = get_engine()

def execute_sql(sql):

    start = time.perf_counter()

    try:
        df = pd.read_sql(sql, engine)

        elapsed = time.perf_counter() - start

        return df, elapsed, None

    except Exception as e:

        return None, None, str(e)