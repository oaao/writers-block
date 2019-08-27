from flask import Flask, request

from helpers import make_genesis_block, make_next_block, initialize_chain


node = Flask(__name__)

node_transactions = []


@node.route('/transaction', methods=['POST'])
def transaction():

    new_transaction = request.get_json()

    node_transactions.append(new_transaction)

    print(
        f'----- NEW TRANSACTION RECEIVED ----\n'
        f'FROM:   {new_transaction["from"]}\n'
        f'TO:     {new_transaction["to"]}\n'
        f'AMOUNT: {new_transaction["amount"]}\n'
    )

    return "transaction successfully submitted"

node.run()

# new_blockchain = initialize_chain(25)
