import datetime

from .objects import Block

def make_genesis_block():

    return Block(
        index=0,
        timestamp=datetime.datetime.now(),
        data='initial commit',
        prev_hash='0'
    )
