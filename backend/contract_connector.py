from web3 import Web3
import json
import os

# Load secrets
w3 = Web3(Web3.HTTPProvider(
    "https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
private_key = os.getenv("PRIVATE_KEY")
account = w3.eth.account.from_key(private_key)

# Load contract ABI
with open("MedOracleABI.json") as f:
    abi = json.load(f)

# Address from Hardhat deployment
contract_address = Web3.to_checksum_address("0xYourDeployedAddress")
contract = w3.eth.contract(address=contract_address, abi=abi)


def store_on_chain(risk, ipfs_cid):
    tx = contract.functions.storeReport(risk, ipfs_cid).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()
