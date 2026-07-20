from sqlalchemy import create_engine

SERVER = r"DESKTOP-SIUL4GP\SQLEXPRESS"
DATABASE = "AI_SQL_Assistant"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

def get_engine():
    return engine