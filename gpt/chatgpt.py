from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)  # take environment variables from .env.

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_content = """ """

user_content = """ """

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": system_content},
    {"role": "user", "content": user_content}
  ]
)

print(completion.choices[0].message.content)