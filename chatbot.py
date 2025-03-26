import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_chatbot_response(prompt: str) -> str:
    try:
        system_message = (
            "You are an expert in developing sui smart contracts using move language. "
            "Generate clear, and concise response that can be integrated into a smart contract template."
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        reply = response["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        raise Exception(f"Error in GPT API call: {e}")