from block import Block
from transaction import Transaction
from rsa import generate_keys, sign, verify

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()
        self.private_key, self.public_key = generate_keys()

    def create_genesis_block(self):
        genesis_block = Block("0", ["Genesis Block"])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(previous_hash, transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                print(f"Block {i} has been tampered!")
                return False
            if current.previous_hash != previous.hash:
                print(f"Block {i} is not linked to Block {i - 1}!")
                return False
        print("Blockchain is valid!")
        return True

    def verify_transaction(self, transaction):
        if not transaction.signature:
            raise ValueError("No signature for transaction")
        return self.chain[-1].verify_transaction(transaction)

class Wallet:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.private_key, self.public_key = generate_keys()

    def create_transaction(self, receiver, amount):
        transaction = Transaction(self.public_key, receiver, amount)
        transaction.sign_transaction(self.private_key)
        return transaction

    def save_transaction(self, transaction, filename="transactions.txt"):
        with open(filename, 'a') as file:
            file.write(str(transaction) + "\n")

    def load_transactions(self, filename="transactions.txt"):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
