import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


class History:

    def __init__(self):
        self.logs = []

    def system(self, message):
        self.add("system", message)

    def assistant(self, message):
        self.add("assistant", message)

    def user(self, message):
        self.add("user", message)

    def add(self, role, message):
        self.logs.append({'role': role, "content": message})

    def count(self):
        return len(self.logs)


def llm_chat(history: History, temperature: float = 0.0):
    response = openai_client.chat.completions.create(
        model="gpt-4o",  # The name of the OpenAI chatbot model to use
        messages=history.logs,  # The conversation history up to this point, as a list of dictionaries
        max_tokens=3000,  # The maximum number of tokens (words or subwords) in the generated response
        stop=None,  # The stopping sequence for the generated response, if any (not used here)
        temperature=temperature,  # The "creativity" of the generated response (higher temperature = more creative)
    )

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content

