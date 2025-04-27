# Multi-Chain Balance Checker

This Python script allows you to check the balances of a given wallet address across multiple blockchain networks. It uses public RPC endpoints to fetch the balance for each chain.

## Features

*   Checks balances across multiple chains: Ethereum, Binance Smart Chain (BSC), Polygon, Arbitrum, Optimism, Avalanche, Fantom, Base, zkSync Era, Linea, Celo, Moonbeam, Moonriver, and Gnosis Chain (xDai).
*   Uses public RPC endpoints for each chain.
*   Saves the results to a `result.txt` file, formatted as: `wallet | Ethereum | BNB | etc`.
*   Option to read wallet addresses from an `address.txt` file (one address per line) or input manually.

## Prerequisites

*   Python 3.6+
*   `web3` library:

    ```bash
    pip install web3
    ```

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/<your-github-username>/multi-chain-balance-checker.git
    cd multi-chain-balance-checker
    ```

2.  Install the required dependencies:

    ```bash
    pip install web3
    ```

## Usage

1.  **Prepare wallet addresses (optional):**
    *   Create a file named `address.txt` in the same directory as the script.
    *   Add one wallet address per line to the `address.txt` file.

2.  **Run the script:**

    ```bash
    python main.py
    ```

    *   If `address.txt` exists, the script will read wallet addresses from the file.
    *   If `address.txt` does not exist, the script will prompt you to enter a wallet address manually.

3.  **View the results:**

    The script will save the balances to a file named `result.txt` in the same directory.  The format is:

    ```
    Wallet | Ethereum Mainnet | Binance Smart Chain (BSC) | Polygon (Matic) | ...
    <wallet_address> | <balance_eth> ETH | <balance_bnb> BNB | <balance_matic> MATIC | ...
    ```

## Configuration

The script uses a predefined list of chains and their corresponding RPC endpoints.  You can modify the `chains` dictionary in `main.py` to add or remove chains, or to use different RPC endpoints.

## Disclaimer

This script uses public RPC endpoints, which may be rate-limited or unreliable. For production use, consider using your own RPC provider.

## Author

[[Ebisidiaidi](https://t.me/ebisidiaidi)]
