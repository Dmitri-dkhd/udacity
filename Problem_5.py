import hashlib
from time import gmtime as gm,strftime as strf

class Node():
        def __init__(self,value):
        	self.value=value
        	self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.previous=""
    def append(self,data):
        head=self.head
        if not self.head:         
            self.head=Node(Block(data))
            self.previous=self.head.value.hash
        else:
            while head.next:
                head=head.next
            
            head.next=Node(Block(data,self.previous))
            self.previous=head.next.value.hash
            
    def __repr__(self):
        head=self.head
        arr=[]
        count=0
        block_data=""
        while head:
            block_data+=f'Block: {count}\nTimestamp: {head.value.timestamp}\nData: {head.value.data}\nHash: {head.value.hash}\nPrevious_hash: {head.value.previous_hash}\n'
            count+=1
            arr.append(block_data)
            head=head.next
        return block_data
                  
class Block:

    def __init__(self, data, previous_hash = "",timestamp = strf('%c',gm())):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
          sha = hashlib.sha256()    
          hash_str = self.timestamp + self.data +self.previous_hash
    
          sha.update(hash_str.encode('utf-8'))
    
          return sha.hexdigest()

blockchain=LinkedList()
for i in range(1000):
	blockchain.append(str(i))
print(blockchain)

