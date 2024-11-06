"""
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
"""
import collections


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    ## Initialize this node in the Trie

    def insert(self, char):
        self.children[char] = TrieNode()

    """
    Finding Suffixes
    Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

    Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)
    """

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        node = self
        if node.is_word:
            return []
        words = []
        self._suffixes(node, suffix, words)
        return words

    def _suffixes(self, node, current_suffix, words):
        if node.is_word and current_suffix:
            words.append(current_suffix)

        for key, current_node in node.children.items():
            self._suffixes(current_node, current_suffix + key, words)


## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions
class Trie:
    ## Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()

    ## Add a word to the Trie
    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
        current.is_word = True

    ## Find the Trie node that represents this prefix
    def find(self, prefix):
        current = self.root
        for char in prefix:
            current = current.children[char]
        return current


trieNode = TrieNode()
trieNode.insert("w")
print("------------")
trie = Trie()
word = "the"
# trie.insert("the")
trie.insert("test")
trie.insert("tea")
trie.insert("teacher")
# print(trie.find(word))
current = trie.root

MyTrie = Trie()
# wordList = ["tea", "teacher"]
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


# interact(f,prefix='');
f("t")
f("f")
f("a")
