import datetime
import json

from flask import Flask, request

import config
from helpers import prove_work, startup
from objects import Block


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

@node.route('/automine', methods=['GET'])
def automine():

    # determine a reference point to begin computing
    latest_block = blockchain[len(blockchain) - 1]
    latest_proof = latest_block.data['proof']

    # once we find a proof, we can compute a block
    # (and transact that client an amount)
    proof = prove_work(latest_proof)

    node_transactions.append(
        {
            'from':  'network',
            'to':     config.CLIENT_ADDRESS,
            'amount': 1
        }
    )

    # and collect the elements needed to generate and apply the next block!

    new_index     = latest_block.index + 1
    new_timestamp = datetime.datetime.now()
    new_data      = {
        'proof':        proof,
        'transactions': node_transactions
    }
    latest_hash   = latest_block.hash
    print(new_data)

    new_block = Block(new_index, new_timestamp, new_data, latest_hash)
    blockchain.append(new_block)

    # provide a descriptive response
    resp = json.dumps(
        {
            'index':     new_index,
            'timestamp': str(new_timestamp),
            'data':      new_data,
            'last_hash': latest_hash
        }
    )

    # before concluding the request,
    # flush out the local transaction cache
    node_transactions[:] = []

    return resp + '\n'


node.run()
