"""
http://chatbot.py - SuiAutoforge Project

This module interfaces with the OpenAI Chat API (using GPT-4) to generate
Sui Move smart contracts based on user prompts. The API key is hardcoded in this
script, and no external dependencies beyond Python's standard library are used.

Note: Replace "YOUR_API_KEY_HERE" with your actual OpenAI API key.
"""

import json
import urllib.request
import urllib.error

# Load environment variables f
API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

def get_sui_contract(prompt):
    """
    Sends a prompt to the OpenAI ChatCompletion API, tailored for generating
    Sui Move smart contracts for the SuiAutoforge project.

    Args:
        prompt (str): A description of the desired contract (e.g., "Generate a token management contract with mint and burn functions")

    Returns:
        str: The generated Sui Move smart contract code or an error message.
    """
    # Prepare the payload with context for generating Sui Move contracts.
    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert in Sui Move smart contract development for the SuiAutoforge project. "
                    "Generate complete and well-structured Sui Move contract code that includes functions such as "
                    "initialize_token, mint_tokens, and burn_tokens. Include placeholders for custom logic where needed."
                )
            },
            {"role": "user", "content": prompt}
        ]
    }

    # Convert the payload to JSON bytes
    data = json.dumps(payload).encode("utf-8")

    # Set HTTP headers with the API key for authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    }

    # Build and send the HTTP request using urllib
    request = urllib.request.Request(API_URL, data=data, headers=headers)
    try:
        with urllib.request.urlopen(request) as response:
            response_data = json.load(response)
            return response_data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as error:
        error_details = error.read().decode()
        return f"HTTP Error {error.code}: {error_details}"
    except Exception as error:
        return f"Error: {str(error)}"

if __name__ == "__main__":
    # For testing purposes: prompt the user and display the generated contract code.
    user_prompt = input("Enter your contract prompt: ")
    contract_code = get_sui_contract(user_prompt)
    print("Generated Sui Move Contract:")
    print(contract_code)