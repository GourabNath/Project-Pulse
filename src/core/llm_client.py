from openai import OpenAI

client = OpenAI()

def generate_response(messages, model="gpt-4.1-nano"):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content
