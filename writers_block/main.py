from flask import Flask, request

from helpers import startup


node = Flask(__name__)

blockchain = startup()

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
