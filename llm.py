from dotenv import load_dotenv
from openai import OpenAI


def generate_answer(client: OpenAI, role: str, question: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content


def generate_question(instruction: str, symptoms: str, example: str) -> str:
    return f"{instruction}\n\nSintomas: '{symptoms}'\n\n{example}"


if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello World"}
        ]
    )
    print(completion.choices[0].message.content)
