import heapq
from collections import defaultdict, namedtuple


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def generate_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)
    return codebook


def huffman_encode(text):
    root = build_huffman_tree(text)
    codebook = generate_codes(root)
    encoded_text = ''.join(codebook[char] for char in text)
    return encoded_text, codebook


def huffman_decode(encoded_text, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ''
    decoded_text = ''

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_text += reverse_codebook[current_code]
            current_code = ''

    return decoded_text


# Example usage
text = "huffman coding example"
encoded_text, codebook = huffman_encode(text)
print("Encoded:", encoded_text)
print("codebook:", codebook)
decoded_text = huffman_decode(encoded_text, codebook)
print("Decoded:", decoded_text)