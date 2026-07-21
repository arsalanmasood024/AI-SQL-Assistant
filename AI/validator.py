import re

FORBIDDEN_KEYWORDS = [
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


def extract_sql(text: str):

    # Remove markdown
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "").strip()

    # Find the first SELECT statement
    match = re.search(
        r"SELECT[\s\S]*",
        text,
        re.IGNORECASE
    )

    if not match:
        return None

    sql = match.group(0).strip()

    # If AI generated another SELECT, keep only the first one
    second = re.search(
        r"\n\s*SELECT",
        sql,
        re.IGNORECASE
    )

    if second:
        sql = sql[:second.start()].strip()

    # Add semicolon if missing
    if not sql.endswith(";"):
        sql += ";"

    return sql


def validate_sql(text: str):

    sql = extract_sql(text)

    if sql is None:
        return False, "No SELECT query found."

    sql_upper = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:

        if re.search(rf"\b{keyword}\b", sql_upper):

            return False, f"Forbidden keyword detected: {keyword}"

    if not sql_upper.startswith("SELECT"):

        return False, "Only SELECT queries are allowed."

    return True, sql