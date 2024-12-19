from transaction import Transaction
from blockchain import Blockchain

if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain(difficulty=3)

    # Add some transactions and blocks
    transactions1 = [
        Transaction("Alice", "Bob", 50),
        Transaction("Bob", "Charlie", 25),
        Transaction("Alice", "Charlie", 30),
        Transaction("Charlie", "Alice", 10),
        Transaction("Eve", "Bob", 45),
        Transaction("Frank", "Eve", 60),
        Transaction("Grace", "Frank", 15),
        Transaction("Alice", "Eve", 35),
        Transaction("Bob", "Grace", 20),
        Transaction("Charlie", "Frank", 40)
    ]
    blockchain.add_block(transactions1)

    transactions2 = [
        Transaction("Charlie", "Alice", 5),
        Transaction("Bob", "Eve", 10),
        Transaction("Eve", "Frank", 15),
        Transaction("Alice", "Bob", 20),
        Transaction("Frank", "Charlie", 25),
        Transaction("Grace", "Eve", 30),
        Transaction("Alice", "Grace", 35),
        Transaction("Bob", "Charlie", 40),
        Transaction("Eve", "Alice", 45),
        Transaction("Frank", "Bob", 50)
    ]
    blockchain.add_block(transactions2)

    # Print the blockchain
    for i, block in enumerate(blockchain.chain):
        print(f"Block {i}:")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print("-" * 50)

    # Validate the blockchain
    blockchain.validate_blockchain()
