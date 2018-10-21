#for timestamps
import datetime
#for hashing algorithms
import hashlib

# defining block data structure.
class Block:
    # let's say each block has 7 attributes

    # 1: block number
    blockNum = 0

    # 2: data (any data you want to store in a block)
    data = None

    # 3: pointer to next block in blockchain
    next = None

    # 4: hash of a block. Unique ID of block and verify its integrity with other blocks
    hash = None

    # 5: nonce is a number only used once
    nouce = 0

    # 6: store hash of previous block in blockchain
    pre_hash = 0x0

    # 7: timestamp
    timestamp = datetime.datetime.now()

    # initialize block by storing data
    def __init__(self,data):
        self.data = data

    # function to generate hash of a block
    # its unique ID and helps make blockchain immutable,
    # ie if one block ID is changed , all the block IDs after 
    # that block will also change (pre_hash).
    def hashFun(self):
        # sha-256 alogrithm that generates unique 256 bit signature
        h = hashlib.sha256()
        
        # input to sha-256 algorithm will be block attributes.
        h.update(
            str(self.nouce).encode('utf-8')+
            str(self.data).encode('utf-8')+
            str(self.pre_hash).encode('utf-8')+
            str(self.timestamp).encode('utf-8')+
            str(self.blockNum).encode('utf-8')
        ) 
        # returns a hex string
        return h.hexdigest()

    # print block data
    def __str__(self):
        return "\nHash: "+ str(self.hashFun()) + "\nBlock No: "+str(self.blockNum)+ "\nData: "+ str(self.data) + "\nNouce: " + str(self.nouce) + "\nPrevious Hash: " + str(self.pre_hash) + "\nTiemstamp: " + str(self.timestamp) +"\n-------------"

# defining the blockchain data structrue
# has block linked together similar to linked list. ohh yeah!
class Blockchain:
    # mining difficulty
    diff = 20

    # max nouce
    maxNouce = 2**32

    # target hash
    targetHash = 2 ** (256-diff) 

    # genearate 1st block
    block = Block("Genesis")

    # set head as this block
    head = block

    # add block to blockchain
    def add(self, block):
        # set this blocks pre_hash to previous blocks hash,
        # which is stored in self.block
        block.pre_hash = self.block.hashFun()

        # increment block number
        block.blockNum = self.block.blockNum + 1

        # set next pointer of previous block to this new block
        self.block.next = block
        self.block = block

    # Determine if we can add a block to the blockchain
    def mine(self, block):
        # from 0 to 2^32 
        for n in range(self.maxNouce):
            # check if the hash is less than our target value
            if int(block.hashFun(),16) <= self.targetHash:
                # if yes, then add
                self.add(block)
                # print(block)
                break
            else:
                block.nouce += 1

blockchain = Blockchain()

# mine 10 blocks
for n in range(10):
    blockchain.mine(Block("Block "+ str(n+1)))

# print out the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next