import hashlib

class Block:
    def __init__(self,data,prev_hash):
        self.data=data
        self.prev_hash=prev_hash
        self.hash=self.calc_hash()
    
    def __repr__(self):
        return f"Data : {self.data}\nHash : {self.hash}\nPrevious Hash : {self.prev_hash}\n"

    def calc_hash(self):#Calculates Hash
        sha=hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain=[Block('Genesis Block','0')]#First block is Genesis Block
    
    def add_block(self,data):
        prev_block=self.chain[-1]
        new_block=Block(data,prev_block.hash)
        self.chain.append(new_block)
    
blockchain=Blockchain()
blockchain.add_block('First Block')
blockchain.add_block('Second Block')
blockchain.add_block('Third Block')

for block in blockchain.chain:
    print(block)