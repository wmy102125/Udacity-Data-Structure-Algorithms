import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = Block.calc_hash(data)

    def __repr__(self):
        return (
                "timestamp:" + self.timestamp + " " + "data:" + self.data + "previous_hash:" + self.previous_hash + "hash:" + self.hash + "\n")

    def calc_hash(str):
        sha = hashlib.sha256()

        hash_str = str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        str = ""
        node = self.data
        node_str =  "timestamp:" + node.timestamp + "\n" + "data:" + node.data + "\n" + "previous_hash:" + node.previous_hash+ "\n"  + "hash:" + node.hash + "\n ------------------------------"
        str = str + node_str
        node = self.next
        while node is not None:
            node_str = "\ntimestamp:" + node.timestamp + "\n" + "data:" + node.data + "\n" + "previous_hash:" + node.previous_hash + "\n" + "hash:" + node.hash + "\n ------------------------------"
            str = str + node_str
            node = node.next
        return str


block = Block(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f%Z"), "Train head", "0")
blockChain = LinkedList(block)
blockChain.next = Block(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f%Z"), "The first Carriage",
                        Block.calc_hash("Train head"))
blockChain.next.next = Block(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f%Z"), "The second Carriage",
                             Block.calc_hash("The first Carriage"))
blockChain.next.next.next = None

print(blockChain)

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3
