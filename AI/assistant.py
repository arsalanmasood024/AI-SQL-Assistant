from AI.sql_generator import generate_sql
from AI.validator import validate_sql
from AI.executor import execute_sql


def ask(question):

    print("\n" + "=" * 60)
    print("QUESTION")
    print("=" * 60)
    print(question)

    # Generate SQL
    sql = generate_sql(question)

    print("\n" + "=" * 60)
    print("GENERATED SQL")
    print("=" * 60)
    print(sql)

    # Validate SQL
    valid, result = validate_sql(sql)

    if not valid:
        print("\n" + "=" * 60)
        print("VALIDATION FAILED")
        print("=" * 60)
        print(result)
        return None

    # Execute SQL
    df, elapsed, error = execute_sql(result)

    if error:
        print("\n" + "=" * 60)
        print("DATABASE ERROR")
        print("=" * 60)
        print(error)
        return None

    # Success
    print("\n" + "=" * 60)
    print("QUERY EXECUTED SUCCESSFULLY")
    print("=" * 60)
    print(f"Execution Time : {elapsed:.3f} seconds")
    print(f"Rows Returned  : {len(df)}")

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(df)

    return df


if __name__ == "__main__":

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        ask(question)