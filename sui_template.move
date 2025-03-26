module SuiToken {
    use std::signer;

    struct Token has key {
        id: u64,
        name: vector<u8>,
        total_supply: u64,
    }

    public fun initialize(account: &signer, name: vector<u8>, total_supply: u64): Token {
        let token = Token {
            id: 0,
            name: name,
            total_supply: total_supply,
        };
        token
    }

    public fun mint_tokens(account: &signer, amount: u64) {
        // Logic to mint tokens
        // For simplicity, assuming a single token instance
        let token = borrow_global_mut<Token>(account.address());
        token.total_supply = token.total_supply + amount;
    }

    public fun burn_tokens(account: &signer, amount: u64) {
        // Logic to burn tokens
        // For simplicity, assuming a single token instance
        let token = borrow_global_mut<Token>(account.address());
        assert!(token.total_supply >= amount, 1);
        token.total_supply = token.total_supply - amount;
    }
}