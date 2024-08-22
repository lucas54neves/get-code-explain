import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You will receive a code and would like a detailed explanation about the code.",  # noqa
        },
        {
            "role": "user",
            "content": """
                import random

                def gerar_numeros_aleatorios(quantidade, limite):
                    numeros = [random.randint(1, limite) for _ in range(quantidade)]
                    return numeros
            """,  # noqa
        },
    ],
)

message = response.choices[0].message.content

print(message)
