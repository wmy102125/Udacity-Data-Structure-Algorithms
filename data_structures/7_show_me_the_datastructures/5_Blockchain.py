import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def __repr__(self):
        return (
                "timestamp:" + self.timestamp + " " + "data:" + self.data + "previous_hash:" + self.previous_hash + "hash:" + self.hash + "\n")

    def calc_hash(self, str):
        sha = hashlib.sha256()

        hash_str = str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
        text = ""
        node = self.head
        while node is not None:
            node_str = "\ntimestamp:" + node.timestamp + "\n" + "data:" + node.data + "\n" + "previous_hash:" + str(node.previous_hash) + "\n" + "hash:" + node.hash + "\n ------------------------------"
            text = text + node_str
            node = node.next
        return text


time = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f%Z")
block = Block(time, "Train head", 0)
blockChain = BlockChain(block)
pre_node = blockChain.head
block2 = Block(time, "Train first carriage", pre_node.hash)
pre_node.next = block2
pre_node = pre_node.next
block3 = Block(time, "Train second carriage", pre_node.hash)
pre_node.next = block3
print(blockChain)
