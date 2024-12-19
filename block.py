import time
from hashing import hash
from merkle_tree import merkle_tree

class Block:
    def __init__(self, previous_hash, transactions, timestamp=None):
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.merkle_root = merkle_tree(transactions)
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_data = str(self.previous_hash) + str(self.timestamp) + str(self.merkle_root) + str(self.nonce)
        return hash(block_data)

    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()
