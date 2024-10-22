import heapq
import sys
from collections import defaultdict


class Node:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_encoding(data):
    data_list = list()
    data_dict = defaultdict(int)
    for char in data:
        data_dict[char] += 1
    for key in data_dict:
        data_list.append(Node(key, data_dict[key]))
    heapq.heapify(data_list)

    while len(data_list) > 1:
        left_node = heapq.heappop(data_list)
        right_node = heapq.heappop(data_list)
        new_node = Node(None, left_node.frequency + right_node.frequency)
        new_node.left = left_node
        new_node.right = right_node
        heapq.heappush(data_list, new_node)

    huffman_code_dict = defaultdict(int)
    huffman_code(data_list[0], '', huffman_code_dict)
    encode_data = ''
    for char in data:
        encode_data += huffman_code_dict[char]
    return encode_data, data_list[0]


def huffman_code(node, prefix_code, huffman_code_dict):
    if node is None:
        return
    if node.key is not None:
        huffman_code_dict[node.key] = prefix_code
    huffman_code(node.left, prefix_code + '0', huffman_code_dict)
    huffman_code(node.right, prefix_code + '1', huffman_code_dict)
    return huffman_code_dict


def huffman_decoding(data, tree):
    return _huffman_decoding("", data, tree, tree)


def _huffman_decoding(content, data, node, tree):
    if node.key is not None:
        content += node.key
        node = tree
    if data == "":
        return content
    if data[0] == '0':
        content = _huffman_decoding(content, data[1:], node.left, tree)
    if data[0] == '1':
        content = _huffman_decoding(content, data[1:], node.right, tree)
    return content


# encodeText, tree = huffman_encoding("The bird is the word")
# print(huffman_decoding(encodeText, tree))


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
def test_function(test_case):
    encode_text,tree = huffman_encoding(test_case)
    decodeText = huffman_decoding(encode_text,tree)
    if test_case == decodeText:
        print("Pass")
    else:
        print("Fail")
## Test Case 1
test_case_1 = "This is a test"
test_function(test_case_1)
## Test Case 2
test_case_2 = ""
test_function(test_case_1)
## Test Case 3
test_case_3 = "12334343"
test_function(test_case_1)
