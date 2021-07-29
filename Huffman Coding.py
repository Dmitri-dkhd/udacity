import sys

class Node:
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
    sorted_container = dict()
    for char in data:
        container[char] = container.get(char, 0) + 1
    # sort the container from lowest to highest value
    while container:
        temp = container[next(iter(container))]
        temp_key = next(iter(container))
        for key, value in container.items():
            if temp > value:
                temp = value
                temp_key = key

        sorted_container[temp_key] = temp
        container.pop(temp_key)

    sorted_container = list(sorted_container.items())
    # define the tree/Node class

    # loop for the huffman tree
    while len(sorted_container) > 1:

        # pop the 2 lowest value elements and create a tree with the sum of their value and the elements as children
        left_child = sorted_container.pop(0)
        right_child = sorted_container.pop(0)

        if type(left_child) == tuple:
            left_value = left_child[1]
        else:
            left_value = left_child.get_head_value()
        if type(right_child) == tuple:
            right_value = right_child[1]
        else:
            right_value = right_child.get_head_value()
        value = right_value + left_value
        tree = Node(value)
        tree.set_right_child(right_child)
        tree.set_left_child(left_child)

        # insert the tree in the list by value
        for index, element in enumerate(sorted_container):

            if type(element) == tuple:
                element_value = element[1]
            else:
                element_value = element.get_head_value()

            if element_value >= value:
                sorted_container.insert(index, tree)

                break

            elif index == len(sorted_container)-1:
                sorted_container.append(tree)
                break

    # traverse the tree to get the code for every char

    def huffman_code(tree):
        code_dict = dict()
        stri = ""

        def traverse(tree, stri):

            if type(tree) == tuple:
                code_dict[tree[0]] = stri

                stri = ""
                return code_dict

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
                decode_dict[stri] = tree[0]

                stri = ""
                return decode_dict

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

    a_great_sentence = '''Data conversion have always been widely used utility and one among them can be
    conversion of a string to it’s binary equivalent. Let’s discuss certain ways in which this can be done.'''

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
