from transaction import Transaction
from blockchain import Blockchain, Wallet

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=3)

    wallet = Wallet(blockchain)

    transaction1 = wallet.create_transaction("receiver_public_key", 50)
    wallet.save_transaction(transaction1)

    blockchain.add_block([transaction1])

    for i, block in enumerate(blockchain.chain):
        print(f"Block {i}:")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print("-" * 50)

    blockchain.validate_blockchain()
