import datetime

from objects import Block


def _proof_placeholder(i, prev_proof, modulo=10):
    return (i % modulo == 0 and i % prev_proof == 0)


def make_genesis_block():

    return Block(
        index=0,
        timestamp=datetime.datetime.now(),
        data='initial commit',
        prev_hash='0'
    )


def make_next_block(prev_block, data=None):

    index     = prev_block.index + 1
    timestamp = datetime.datetime.now()
    next_hash = prev_block.hash

    if not data:
        data = f'This is block #{index}'

    return Block(index, timestamp, data, next_hash)


def initialize_chain(num_blocks):

    # account for 'free' genesis block
    n = num_blocks - 1

    print(f'Initializing blockchain with {n} blocks\n')

    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]

    for i in range(num_blocks):

        block = make_next_block(prev_block)
        blockchain.append(block)

        print(
            f'Block #{block.index} has been added to blockchain [ length: {len(blockchain)} ]\n'
            f'Hash: {block.hash}\n'
        )

        prev_block = block

    return blockchain

def prove_work(prev_proof):

    i = prev_proof + 1

    while not _proof_placeholder(i, prev_proof):
        i + 1

    return i
