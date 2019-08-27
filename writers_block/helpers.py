import datetime
import inquirer

from objects import Block


def startup():

    configs = [
        inquirer.List(
            'new',
            message='Are you generating a new blockchain or participating in an existing one?',
            choices=['new blockchain', 'existing blockchain'],
            default='new blockchain'
        ),

        inquirer.Text(
            'num',
            message='How many blocks should be generated in the initial chain?',
            default='10',
        ),
    ]

    start = inquirer.prompt(configs)

    if start['new'] == 'new blockchain':
        return initialize_chain(int(start['num']))
    else:
        return []

def _placeholder_algorithm(i, prev_proof, modulo=10):
    return (i % modulo == 0 and i % prev_proof == 0)

def prove_work(prev_proof):

    i = prev_proof + 1

    while not _placeholder_algorithm(i, prev_proof):
        i += 1

    return i


def make_genesis_block():

    genesis = Block(
        index=0,
        timestamp=datetime.datetime.now(),
        data={'proof': 1},
        prev_hash='0'
    )

    print(
        f'Genesis block has been added to blockchain [ length: 1 ]\n'
        f'Hash: {genesis.hash}\n'
    )

    return genesis


def make_next_block(prev_block, data=None):

    index     = prev_block.index + 1
    timestamp = datetime.datetime.now()
    next_hash = prev_block.hash

    if not data:
        data = {'proof': prove_work(prev_block.data['proof'])}

    return Block(index, timestamp, data, next_hash)


def initialize_chain(num_blocks):

    # account for 'free' genesis block
    n = num_blocks - 1

    print(f'Initializing blockchain with {num_blocks} blocks\n')

    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]

    for i in range(n):

        block = make_next_block(prev_block)
        blockchain.append(block)

        print(
            f'Block #{block.index} has been added to blockchain [ length: {len(blockchain)} ]\n'
            f'Hash: {block.hash}\n'
        )

        prev_block = block

    return blockchain

