from ollama import chat


def explain_sql(sql):

    prompt = f"""
Explain the following SQL query in simple English.

Keep it under 80 words.

SQL:

{sql}
"""

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]