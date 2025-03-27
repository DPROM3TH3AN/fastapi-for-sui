"""
contract_generator.py - SuiAutoforge Project

This module generates complete Sui Move smart contracts by reading a base template
(sui_template.move) from the same folder and injecting generated contract logic into it.
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
            return file.read()  # Fixed incorrect method call
    except FileNotFoundError:
        print(f"Error: Template file '{template_filename}' not found.")
        return None

def generate_contract(template_content: str, generated_logic: str) -> str:
    """
    Injects the generated contract logic into the template content by replacing the placeholder.

    Args:
        template_content (str): The base template content.
        generated_logic (str): The generated logic to insert into the template.

    Returns:
        str: The complete contract code.

    Raises:
        ValueError: If the placeholder '{contract_logic}' is not found in the template content.
    """
    if "{contract_logic}" not in template_content:
        raise ValueError("Error: Placeholder '{contract_logic}' not found in the template content.")
    # Replace the placeholder '{contract_logic}' with the actual generated logic.
    complete_contract = template_content.replace("{contract_logic}", generated_logic)
    return complete_contract

def save_contract(contract_content: str, output_filename: str):
    """
    Saves the generated contract content to a specified file.

    Args:
        contract_content (str): The content of the generated contract.
        output_filename (str): The filename to save the contract to.
    """
    try:
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(contract_content)
        print(f"Contract successfully saved to '{output_filename}'.")
    except IOError as e:
        print(f"Error: Unable to save contract to '{output_filename}'. {e}")

# For standalone testing:
if __name__ == "__main__":
    sample_logic = (
        "// Custom initialization logic\n"
        "move_to<Token>(account, token);\n"  # Fixed incorrect HTML entity
        "// Minting logic\n"
        "let token_ref = borrow_global_mut<Token>(signer::address_of(account));\n"  # Fixed incorrect HTML entity
        "token_ref.total_supply = token_ref.total_supply + amount;\n"
        "// Burning logic\n"
        "assert!(token_ref.total_supply >= amount, 1);\n"  # Fixed incorrect HTML entity
        "token_ref.total_supply = token_ref.total_supply - amount;\n"
    )
    template = load_template("sui_template.move")
    if template:
        final_contract = generate_contract(template, sample_logic)
        print("Generated Contract:\n", final_contract)
        save_contract(final_contract, "generated_contract.move")  # Save the generated contract