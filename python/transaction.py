from rsa import sign

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.amount} | Signature: {self.signature}"

    def sign_transaction(self, private_key):
        message = f"{self.sender}{self.receiver}{self.amount}"
        self.signature = sign(private_key, message)
