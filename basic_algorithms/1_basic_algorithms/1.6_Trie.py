# ##solution
# class TrieNode(object):
#     def __init__(self):
#         self.is_word = False
#         self.children = {}
#
#
# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
#
#     def add(self, word):
#         """
#         Add `word` to trie
#         """
#         current_node = self.root
#
#         for char in word:
#             if char not in current_node.children:
#                 current_node.children[char] = TrieNode()
#             current_node = current_node.children[char]
#
#         current_node.is_word = True
#
#     def exists(self, word):
#         """
#         Check if word exists in trie
#         """
#         current_node = self.root
#
#         for char in word:
#             if char not in current_node.children:
#                 return False
#             current_node = current_node.children[char]
#
#         return current_node.is_word
# word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
# word_trie = Trie()
#
# # Add words
# for word in word_list:
#     word_trie.add(word)
#
# # Test words
# test_words = ['bear', 'goo', 'good', 'goos']
# for word in test_words:
#     if word_trie.exists(word):
#         print('"{}" is a word.'.format(word))
#     else:
#         print('"{}" is not a word.'.format(word))


"""
## Trie using Defaultdict (Optional)
This is an optional section. Feel free to skip this and go to the next section of the classroom.

A cleaner way to build a trie is with a Python default dictionary. The following `TrieNod` class is using `collections.defaultdict` instead of a normal dictionary.
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        if word is None:
            return
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        if word is None:
            return False
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word


# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')
