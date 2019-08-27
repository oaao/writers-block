import datetime

from objects import Block


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
