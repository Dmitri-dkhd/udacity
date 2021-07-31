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
    container = dict()
    
    for char in data:
        container[char] = container.get(char, 0) + 1
    
    # loop for the huffman tree
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
            else:
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
            else:
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

    a_great_sentence = '''567'''

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
