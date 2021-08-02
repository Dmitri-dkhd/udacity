The blocks themselves do not contain the information about the next block
and they only store the previous hash, therefore they are stored in a linked list.
The time efficiency for a block
is determined by the calc_hash method, where the sha256 hashing is running at least in linear time.
The repr method of Linkedlist is also O(n).
The space efficiency of a block is constant and Linear for the LinkedList.
