import openai
from data.config import OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

def send_request(prompt):
    try:
        response = openai.ChatCompletion.create(
          model="gpt-2",
          messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {e}"

