from hashing import hash

def merkle_tree(transactions):
    if len(transactions) % 2 != 0:
        transactions.append(transactions[-1])

    hashed_transactions = [hash(str(tx)) for tx in transactions]

    while len(hashed_transactions) > 1:
        if len(hashed_transactions) % 2 != 0:
            hashed_transactions.append(hashed_transactions[-1])

        temp = []
        for i in range(0, len(hashed_transactions), 2):
            combined = hashed_transactions[i] + hashed_transactions[i + 1]
            temp.append(hash(combined))
        hashed_transactions = temp

    return hashed_transactions[0] if hashed_transactions else None
