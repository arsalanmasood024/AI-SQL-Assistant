FORBIDDEN = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "EXEC",
    "MERGE",
    "GRANT",
    "REVOKE",
]


def validate_sql(sql: str):

    sql_upper = sql.upper()

    for keyword in FORBIDDEN:

        if keyword in sql_upper:

            return False, f"Forbidden SQL detected: {keyword}"

    if not sql_upper.strip().startswith("SELECT"):

        return False, "Only SELECT queries are allowed."

    return True, "Valid SQL"