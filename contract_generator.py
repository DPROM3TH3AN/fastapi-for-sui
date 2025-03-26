from typing import Optional

def generate_contract(
        chatbot_response: str, template_file: str = "template/sui_template.move") -> str:
    try:
        with open(template_file, "r") as file:
            contract_template = file.read()
        contract_code = contract_template.replace("{contract_logic}", chatbot_response)
        return contract_code
    except FileNotFoundError:
        raise Exception(f"Template file not found: {template_file}")
    except Exception as e:
        raise Exception(f"Error generating contract: {e}")

def generate_contract_code(data):
    template = open("template/sui_template.move", "r").read()
    return template.replace("{VARIABLE}", data["input"])