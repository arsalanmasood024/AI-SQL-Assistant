import os

from openai import OpenAI

from dotenv import load_dotenv

from .prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_sql(question):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

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

        temperature=0

    )

    sql = response.choices[0].message.content.strip()

    return sql


if __name__ == "__main__":

    question = "Show top 10 customers"

    sql = generate_sql(question)

    print(sql)