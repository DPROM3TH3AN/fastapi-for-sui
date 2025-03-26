"""
contract_generator.py - SuiAutoforge Project

This module generates complete Sui Move smart contracts by reading a base template (sui_template.move)
from the same folder and injecting generated contract logic in place of the placeholder '{contract_logic}'.
"""

def load_template(template_filename="sui_template.move"):
    """
    Loads the Sui Move contract template from the current directory.

    Args:
        template_filename (str): The filename of the template. Defaults to "sui_template.move".

    Returns:
        str: The contents of the template file.
    """
    try:
        with open(template_filename, "r", encoding="utf-8") as file:
            return file.read()  # Fixed incorrect usage of http://
    except FileNotFoundError:
        print(f"Error: Template file '{template_filename}' not found.")
        return None

def generate_contract(template_content, generated_logic):
    """
    Injects the generated contract logic into the template content by replacing the placeholder.

    Args:
        template_content (str): The base template content.
        generated_logic (str): The generated logic to insert into the template.

    Returns:
        str: The complete contract code.
    """
    # Replace the placeholder '{contract_logic}' with the actual generated logic.
    complete_contract = template_content.replace("{contract_logic}", generated_logic)
    return complete_contract

if __name__ == "__main__":
    # Example generated logic; in practice, this might come from an AI model or another module.
    test_generated_logic = (
        "// Custom initialization logic: store the token resource in the account's storage.\n"
        "store<Token>(account, token);\n\n"
        "// Additional minting logic: update the token's total supply.\n"
        "token.total_supply = token.total_supply + amount;\n\n"
        "// Additional burning logic: ensure the amount is valid before reducing supply.\n"
        "assert!(token.total_supply >= amount, 1);\n"
        "token.total_supply = token.total_supply - amount;\n"
    )
    
    # Load the template from the same folder.
    template = load_template("sui_template.move")
    if template is not None:
        final_contract = generate_contract(template, test_generated_logic)
        print("Generated Sui Move Contract:\n")
        print(final_contract)