import os
from web3 import Web3

# --- List of Chains with Public RPCs ---
chains = {
    "Ethereum Mainnet": {
        "rpc": "https://eth.llamarpc.com",
        "symbol": "ETH",
    },
    "Binance Smart Chain (BSC)": {
        "rpc": "https://bsc-dataseed.binance.org/",
        "symbol": "BNB",
    },
    "Polygon (Matic)": {
        "rpc": "https://polygon-rpc.com/",
        "symbol": "MATIC",
    },
    "Arbitrum One": {
        "rpc": "https://arb1.arbitrum.io/rpc",
        "symbol": "ETH",
    },
    "Optimism": {
        "rpc": "https://mainnet.optimism.io",
        "symbol": "ETH",
    },
    "Avalanche C-Chain": {
        "rpc": "https://api.avax.network/ext/bc/C/rpc",
        "symbol": "AVAX",
    },
}

# --- Function to fetch and display balances ---
def get_balance(chain_name, rpc_url, symbol, address, results):
    try:
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not web3.is_connected():
            print(f"[!] Failed to connect to {chain_name}")
            return

        checksum_address = web3.to_checksum_address(address)
        balance_wei = web3.eth.get_balance(checksum_address)
        balance_eth = Web3.from_wei(balance_wei, 'ether')

        if balance_eth > 0:
            balance_str = f"{balance_eth:.6f} {symbol}"
            print(f"{chain_name:30}: {balance_str}")
            results[chain_name] = balance_str
        else:
            print(f"{chain_name:30}: 0 {symbol}")
            results[chain_name] = f"0 {symbol}"

    except Exception as e:
        print(f"[!] Error on {chain_name}: {e}")
        results[chain_name] = "Error"

# --- Main execution ---
if __name__ == "__main__":
    wallet_addresses = []
    if os.path.exists("address.txt"):
        with open("address.txt", "r") as f:
            wallet_addresses = [line.strip() for line in f.readlines()]
    else:
        # --- Ask user for wallet address ---
        wallet_addresses = [input("Enter your wallet address: ").strip()]

    print("\n🔎 Checking balances across multiple chains...\n")

    with open("result.txt", "w") as outfile:
        header = "Wallet | " + " | ".join(chains.keys()) + "\n"
        outfile.write(header)

        for wallet_address in wallet_addresses:
            print(f"\n--- Balances for address: {wallet_address} ---\n")
            results = {}
            for chain_name, data in chains.items():
                get_balance(chain_name, data['rpc'], data['symbol'], wallet_address, results)

            result_line = wallet_address + " | " + " | ".join(results.values()) + "\n"
            outfile.write(result_line)

    print("\nBalances saved to result.txt")


