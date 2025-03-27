"""
contract_generator.py - SuiAutoforge Project

This module generates complete Sui Move smart contracts by reading a base template
(sui_template.move) from the same folder and injecting generated contract logic into it.
The template must include the placeholder "{contract_logic}" where the custom logic is inserted.
"""

def load_template(template_filename="sui_template.move") -> str:
    """
    Loads the Sui Move contract template from the current directory.
    
    Args:
        template_filename (str): The filename of the template. Defaults to "sui_template.move".
        
    Returns:
        str: The contents of the template file.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: If any other error occurs during file loading.
    """
    try:
        with open(template_filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file '{template_filename}' not found.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the template: {str(e)}")

def generate_contract(template: str, contract_logic: str) -> str:
    """
    Injects the generated contract logic into the template by replacing the placeholder.
    
    Args:
        template (str): The base template content.
        contract_logic (str): The generated logic to insert into the template.
        
    Returns:
        str: The complete contract code.
        
    Raises:
        ValueError: If the placeholder "{contract_logic}" is not found in the template.
    """
    placeholder = "{contract_logic}"
    if placeholder not in template:
        raise ValueError(f"Error: placeholder '{placeholder}' not found in the template content.")
    return template.replace(placeholder, contract_logic)

if __name__ == "__main__":
    # For standalone testing of the contract generator.
    sample_logic = (
        "// Custom initialization logic: store the token resource\n"
        "move_to<Token>(account, token);\n\n"
        "// Minting logic: increase total supply\n"
        "let token_ref = borrow_global_mut<Token>(signer::address_of(account));\n"
        "token_ref.total_supply = token_ref.total_supply + amount;\n\n"
        "// Burning logic: check supply and reduce\n"
        "assert!(token_ref.total_supply >= amount, 1);\n"
        "token_ref.total_supply = token_ref.total_supply - amount;\n"
    )
    
    template = load_template("sui_template.move")
    final_contract = generate_contract(template, sample_logic)
    print("Generated Contract:\n", final_contract)