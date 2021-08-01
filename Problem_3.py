import sys

class Tree:
    def __init__(self, head):
        self.head = head
        self.left_child = None
        self.right_child = None

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def set_left_child(self, left_child):
        self.left_child = left_child

    def get_head_value(self):
        return self.head

    def __repr__(self):
        return f"Node.head: {self.head}"


def huffman_encoding(data):
    if not data:
        return None,None
    container = dict()
    
    for char in data:
        container[char] = container.get(char, 0) + 1
    
    # loop for the huffman tree
    if len(container)==1:
        tree=Tree(container[next(iter(container))])
        tree.set_left_child((next(iter(container)),container[next(iter(container))]))
        
    else:
        while len(container) > 1:
            # pop the 2 lowest value elements and create a tree with the sum of their value and the elements as children
            mi=min(container,key = lambda key: container[key])
            left_child = (mi,container.pop(mi))
            mi=min(container,key = lambda key: container[key])
            right_child = (mi,container.pop(mi))
            
            value = right_child[1] + left_child[1]
            tree = Tree(value)
            tree.set_right_child(right_child)
            tree.set_left_child(left_child)
            container[tree]=tree.get_head_value()
        
    def huffman_code(tree): # traverse the tree to get the code for every char
        
        code_dict = dict()
        stri = ""

        def traverse(tree, stri):
            
            if type(tree) == tuple:
                if type(tree[0])==str:
                    code_dict[tree[0]] = stri

                    stri = ""
                    
                    return code_dict

                traverse(tree[0].get_left_child(), stri+'0')
                traverse(tree[0].get_right_child(), stri+'1')
            elif type(tree)==Tree:
                traverse(tree.get_left_child(), stri+'0')
                traverse(tree.get_right_child(), stri+'1')
            return code_dict
        
        traverse(tree, stri)
        code_string = ''
        for char in data:
            if char in code_dict:
                code_string += code_dict[char]

        binary_code = format(int(code_string, base=2), f'0{len(code_string)}b')
        return binary_code

    binary_code = huffman_code(tree)
    
    return binary_code, tree

def huffman_decoding(data, tree):
    if not data:
        return None
    def huffman_decode(tree):
        decode_dict = dict()
        stri = ""

        def traverse(tree, stri):
            
            if type(tree) == tuple:
                if type(tree[0])==str:
                    decode_dict[stri] = tree[0]

                    stri = ""
                    return decode_dict

                traverse(tree[0].get_left_child(), stri+'0')
                traverse(tree[0].get_right_child(), stri+'1')
            elif type(tree)==Tree:
                traverse(tree.get_left_child(), stri+'0')
                traverse(tree.get_right_child(), stri+'1')
            return decode_dict

        traverse(tree, stri)
        return decode_dict
    
    decode_dict = huffman_decode(tree)
    data_string = str(data)
    new_string = ""
    decoded_data = ""
    for char in data_string:      
        new_string += char
        if new_string in decode_dict:
            decoded_data += decode_dict[new_string]
            new_string = ""
    
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = '''-BY RUDYARD KIPLING: IF
If you can keep your head when all about you   
    Are losing theirs and blaming it on you,   
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;   
If you can wait and not be tired by waiting,
    Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
    And yet don’t look too good, nor talk too wise:

If you can dream—and not make dreams your master;   
    If you can think—and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth you’ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build ’em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: ‘Hold on!’

If you can talk with crowds and keep your virtue,   
    Or walk with Kings—nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty seconds’ worth of distance run,   
Yours is the Earth and everything that’s in it,   
    And—which is more—you’ll be a Man, my son!
    '''

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    print('________________________________________')

    a_great_sentence = None #should return None

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    print('________________________________________')

    a_great_sentence = '''::::::::::'''

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    if encoded_data:
        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
