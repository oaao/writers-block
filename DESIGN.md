# design ideation

Initial scope up until sending/receiving.

## objects

A **block object**, with the following attributes:
```
- a timestamp
- an index (optional)
- a hash, which hashes:
    + the block's data
    + the block's timestamp
    + the block's index
    + the hash of the previous block's hash
```

A **blockchain**, which stores `Block` instances:
```
- a list (of Block() objects)
```


A **data format** for a "transaction", with the following attributes:
```
- sender
- receiver
- amount
```

An **HTTP server** which acts as a node:
```
- using Flask
- store incoming records of new transactions (accept only 'POST')
- get the last block/proof to do new work    (accept only 'GET')
```

## actions

1. **Generate the initial block** (zero-index "genesis block")
2. **Generate successive blocks**
3. **Generate transaction data**
4. **Produce proof of work**
5. **Create a consensus condition** that preserves the longest chain in the network.
