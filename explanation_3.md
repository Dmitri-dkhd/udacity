Dictionary was chosen as the container, because every character that has to be stored is unique and their count in 'data' can be managed in key: value pairs.
To get the required binary encoding the tree traversal had to be Depth First Search. 
The crucial efficiency is the while loop in line 42 in combination with the min-function the overall efficiency is O(n²).
The overall space efficiency is O(n) by storing the data in a dict and storing decoded data.

