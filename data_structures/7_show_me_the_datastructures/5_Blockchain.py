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
        try:
            hash_str = str.encode('utf-8')
            sha.update(hash_str)
        except Exception:
            print("the str can't be null before get the hashcode")

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, block):
        if self.head is None:
            self.head = block
            self.tail = self.head
        else:
            self.tail.next = block
            self.tail.next.previous_hash = self.tail.hash
            self.tail = self.tail.next

    def __repr__(self):
        text = ""
        node = self.head
        while node is not None:
            node_str = "\ntimestamp:" + node.timestamp + "\n" + "data:" + node.data + "\n" + "previous_hash:" + str(
                node.previous_hash) + "\n" + "hash:" + node.hash + "\n ------------------------------"
            text = text + node_str
            node = node.next
        return text


time = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f%Z")
block = Block(time, "Train head", 0)
block2 = Block(time, "Train first carriage",None)
block3 = Block(time, "Train second carriage",None)
blockChain = BlockChain()
blockChain.append(block)
blockChain.append(block2)
blockChain.append(block3)
#test_case_1
test_case = blockChain
node = test_case.head
pre_hash = node.hash
next_pre_hash = node.next.previous_hash
print("Pass" if pre_hash == next_pre_hash else "Fail")

# test_case_2,the str can't be null before get the hashcode
blockChain = BlockChain()
block2 = Block(time, None,None)
blockChain.append(block2)



#
# blockChain = BlockChain(None)
# block3 = Block(time, "head is None", pre_node.hash)
# test_case = blockChain
# print(test_case)
