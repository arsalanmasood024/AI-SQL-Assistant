import ollama
from AI.prompt import SYSTEM_PROMPT

MODEL = "llama3.2:3b"


def generate_sql(question: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        options={
            "temperature": 0
        }   

    )
    response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ],
    options={
        "temperature": 0
    }
)

    return response["message"]["content"].strip()



if __name__ == "__main__":

    question = "Show top 10 customers by total sales"

    sql = generate_sql(question)

    print("\nGenerated SQL:\n")
    print(sql)