It was the best choise to use a dictionary datastructure 
for this problem.
Dictionaries are ordered, and have average time for access, delete
and search of O(1).
The simple idea of 'get' by searching for the key
in the dictionary was modified deleting the access key-value pair
and adding the same key value pair again to renew the order of last used items.
'set' had to be modified with a comparison of the lenght of the dictionary with
the capacity input. By full capacity, the first iterate of the dictionary is removed.  
