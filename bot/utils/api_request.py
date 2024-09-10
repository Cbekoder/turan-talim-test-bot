from data.config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def send_request(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

