"""A Tutorial on HashMap
(In addition to having fun) We write programs to solve real world problems. Data structures help us in representing and efficiently manipulating the data associated with these problems.

Let us see if we can use any of the data structures that we already know to solve the following problem

The Problem Scenario
In a class of students, store heights for each student.

The problem in itself is very simple. We have the data of heights of each student. We want to store it so that next time someone asks for height of a student, we can easily return the value. But how can we store these heights?

Obviously we can use a database and store these values. But, let's say we don't want to do that for now. We want to use a data structure to store these values as part of our program. For the sake of simplicity, our problem is limited to storing heights of students. But you can certainly imagine scenarios where you have to store such key-value pairs and later on when someone gives you a key, you can efficiently return the corrresponding value.

The class diagram for HashMaps would look something like this.

class HashMap:

    def __init__(self):
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def size(self):
        return self.num_entries
Arrays
Can we use arrays to store key-value pairs?

We can certainly use one array to store the names of the students and use another array to store their corresponding heights at the corresponding indices.

What will be the time complexity in this scenario?

To obtain height of a student, say Potter, Harry, we will have to traverse the entire array and check if the value at a particular index matches Potter, Harry. Once we find the index in which this value is stored, we can use this index to obtain the height from the second array.

Thus, because of this traveral, complexity for get() operation becomes 𝑂(𝑛)
. Even if we maintain a sorted array, the operation will not take less than 𝑂(𝑙𝑜𝑔(𝑛))
 complexity.

What happens if a student leaves a class? We will have to delete the entry corresponding to the student from both the arrays.

This would require another traversal to find the index. And then we will have to shift our entire array to fill this gap. Again, the time complexity of operation becomes 𝑂(𝑛)

Linked List
Is it possible to use linked lists for this problem?

We can certainly modify our LinkedListNode to have two different value attributes - one for name of the student and the other for height.

But we again face the same problem. In the worst case, we will have to traverse the entire linked list to find the height of a particular student. Once again, the cost of operation becomes 𝑂(𝑛)
.

Stacks and Queues
Stacks and Queues are LIFO and FIFO data structures respectively. Can you think why they too do not make a good choice for storing key-value pairs?

Can we do better? Can you think of any data structure that allows for fast get() operation?

Let us circle back to arrays.

When we obtain the element present at a particular index using something like arr[3], the operation takes constant i.e. O(1) time.

For review - Does this constant time operation require further explanation?

If we think about array indices as keys and the element present at those indices as values, we can fairly conclude that at least for non-zero integer keys, we can use arrays.

However, like our current problem statement, we may not always have integer keys.

If only we had a function that could give us arrays indices for any key value that we gave it!

Hash Functions
Simply put, hash functions are these really incredible magic functions which can 6_map data of any size to a fixed size data. This fixed sized data is often called hash code or hash digest.

Let's create our own hash function to store strings

def hash_function(string):
    pass
For a given string, say abcd, a very simple hash function can be sum of corresponding ASCII values.

Note: you can use ord(character) to determine ASCII value of a particular character e.g. ord('a') will return 97

def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code

hash_code_1 = hash_function("abcd")
print(hash_code_1)
394
Looks like our hash function is working fine. But is this really a good hash function?

For starters, it will return the same value for abcd and bcda. Do we want that? We can create 24 different permutations for the string abcd and each will have the same value. We cannot put 24 values to one index.

Obviously, this makes it clear that our hash function must return unique values for unique objects.

When two different inputs produce the same output, then we have something called a collision. An ideal hash function must be immune from producing collisions.

Let's think something else.

Can product help? We will again run in the same problem.

The honest answer is that we have differernt hash functions for different types of keys. The hash function for integers will be different from the hash function for strings, which again, will be different for some object of a class that you created.

However, let's try to continue with our problem and try to come up with a hash function for strings.

Hash Function for Strings
For a string, say abcde, a very effective function is treating this as number of prime number base p. Let's elaborate this statement.

For a number, say 578, we can represent this number in base 10 number system as
5∗102+7∗101+8∗100

Similarly, we can treat abcde in base p as
𝑎∗𝑝4+𝑏∗𝑝3+𝑐∗𝑝2+𝑑∗𝑝1+𝑒∗𝑝0

Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and this hash function is one of the most popular functions used for strings. We use prime numbers because the provide a good distribution. The most common prime numbers used for this function are 31 and 37.

Thus, using this algorithm, we can get a corresponding integer value for each string key and use it as an index of an array, say bucket array. It is not a special array. We simply choose to give a special name to arrays for this purpose. Each entry in this bucket array is called a bucket and the index in which we store a bucket is called bucket index. You can visualize the bucket array as shown in the figure below:



Let's add these details to our class."""

#
# class HashMap:
#
#     def __init__(self, initial_size=10):
#         self.bucket_array = [None for _ in range(initial_size)]
#         self.p = 37  # a prime numbers
#         self.num_entries = 0
#
#     def put(self, key, value):
#         pass
#
#     def get(self, key):
#         pass
#
#     # Returns the bucket_index
#     def get_bucket_index(self, key):
#         return self.get_hash_code(key)  # The returned hash code will be the bucket_index
#
#     # Returns the hash code
#     def get_hash_code(self, key):
#         key = str(key)
#
#         # represents (self.p^0) which is 1
#         current_coefficient = 1
#
#         hash_code = 0
#
#         for character in key:
#             hash_code += ord(character) * current_coefficient
#             current_coefficient *= self.p
#
#         return hash_code  # The generated hash code will be the bucket_index
#
#
# hash_map = HashMap()
#
# bucket_index = hash_map.get_bucket_index("abcd")
# print(bucket_index)
#
# hash_map = HashMap()
#
# bucket_index = hash_map.get_bucket_index("bcda")
# print(bucket_index)
#
# class HashMap:
#
#     def __init__(self, initial_size=10):
#         self.bucket_array = [None for _ in range(initial_size)]
#         self.p = 31
#         self.num_entries = 0
#
#     def put(self, key, value):
#         pass
#
#     def get(self, key):
#         pass
#
#     def get_bucket_index(self, key):
#         bucket_index = self.get_hash_code(key)  # The returned hash code will be the bucket_index
#         return bucket_index
#
#     def get_hash_code(self, key):
#         key = str(key)
#         num_buckets = len(self.bucket_array)  # length of array to be used in Mod operation
#
#         current_coefficient = 1  # represents (self.p^0) which is 1
#
#         hash_code = 0
#
#         for character in key:
#             hash_code += ord(character) * current_coefficient
#             hash_code = hash_code % num_buckets  # compress hash_code (Mod operation)
#             current_coefficient *= self.p
#             current_coefficient = current_coefficient % num_buckets  # compress coefficient as well
#
#         return hash_code % num_buckets  # one last compression before returning
#
#     def size(self):
#         return self.num_entries
#
# # Check the bucket_index for two different strings made with same set of characters
# hash_map = HashMap()
#
# bucket_index = hash_map.get_bucket_index("one")
# print(bucket_index)
#
# bucket_index = hash_map.get_bucket_index("neo")
# print(bucket_index)                                  # Collision might occur
#
# class LinkedListNode:
#
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class HashMap:
#
#     def __init__(self, initial_size=10):
#         self.bucket_array = [None for _ in range(initial_size)]
#         self.p = 31
#         self.num_entries = 0
#
#     '''
#     Separate chaining:
#     In case of collision, the `put()` function uses the same bucket to store a linked list of key-value pairs.
#     Every bucket will have it's own separate chain of linked list nodes.
#     '''
#
#     def put(self, key, value):  # The key is a string, and value is numeric
#         bucket_index = self.get_bucket_index(key)
#
#         new_node = LinkedListNode(key, value)  # Create a node
#         head = self.bucket_array[bucket_index]  # Create a reference that points to the existing bucket at position bucket_index
#
#         # Check if key is already present in the 6_map, and UPDATE it's value
#         # Remember, a key should always be unique.
#         while head is not None:
#             if head.key == key:
#                 head.value = value
#                 return
#             head = head.next
#
#         '''
#         If the key is a new one, hence not found in the chain (LinkedList), then following two cases arise:
#          1. The key has generated a new bucket_index
#          2. The key has generated an existing bucket_index.
#             This event is a Collision, i.e., two different keys have same bucket_index.
#
#         In both the cases, we will prepend the new node (key, value) at the beginning (head) of the chain (LinkedList).
#         Remember that each `bucket` at position `bucket_index` is actually a chain (LinkedList) with 1 or more nodes.
#         '''
#         head = self.bucket_array[bucket_index]
#         new_node.next = head
#         self.bucket_array[bucket_index] = new_node  # Prepend the new node in the beginning of the linked list
#         self.num_entries += 1
#
#     def get(self, key):
#         bucket_index = self.get_bucket_index(key)
#         head = self.bucket_array[bucket_index]
#         while head is not None:
#             if head.key == key:
#                 return head.value
#             head = head.next
#         return None
#
#     def get_bucket_index(self, key):
#         bucket_index = self.get_hash_code(key)
#         return bucket_index
#
#     def get_hash_code(self, key):
#         key = str(key)
#         num_buckets = len(self.bucket_array)
#         current_coefficient = 1
#         hash_code = 0
#         for character in key:
#             hash_code += ord(character) * current_coefficient
#             hash_code = hash_code % num_buckets  # compress hash_code
#             current_coefficient *= self.p
#             current_coefficient = current_coefficient % num_buckets  # compress coefficient
#
#         return hash_code % num_buckets  # one last compression before returning
#
#     def size(self):
#         return self.num_entries
#
#     # Helper function to see the hashmap
#     def __repr__(self):
#         output = "\nLet's view the hash 6_map:"
#
#         node = self.bucket_array
#         for bucket_index, node in enumerate(self.bucket_array):
#             if node is None:
#                 output += '\n[{}] '.format(bucket_index)
#             else:
#                 output += '\n[{}]'.format(bucket_index)
#                 while node is not None:
#                     output += ' ({} , {}) '.format(node.key, node.value)
#                     if node.next is not None:
#                         output += ' --> '
#                     node = node.next
#
#         return output
#
# # Test the collision resolution technique
# hash_map = HashMap()
#
# hash_map.put("one", 1)
# hash_map.put("two", 2)
# hash_map.put("three", 3)          # Collision: The key "three" will generate the same bucket_index as that of the key "two"
# hash_map.put("neo", 11)           # Collision: The key "neo" will generate the same bucket_index as that of the key "one"
#
# print("size: {}".format(hash_map.size()))
#
# print("one: {}".format(hash_map.get("one")))
# print("neo: {}".format(hash_map.get("neo")))
# print("three: {}".format(hash_map.get("three")))
#
# hash_map                          # call to the helper function to see the hashmap

#Rehashing code
class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the 6_map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
    def  delete_mine (self,key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        if head is None:
            return
        if head.key == key:
            self.bucket_array[bucket_index] = head.next
            head = None
            self.num_entries -= 1
            return
        while head.next is not None:
            if head.next.key == key:
                node = head.next
                head.next = head.next.next
                node = None
                self.num_entries -= 1
            head = head.next

    """Delete Operation
Can you implement delete operation using all we have learnt so far?"""
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient
        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)  # we can use our put() method to rehash
                head = head.next

    # Helper function to see the hashmap
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash 6_map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next

        return output


# Test Rehashing

# We have reduced the size of the hashmap array to increase the load factor (> 0.7)
# and hence trigger the rehash() function
hash_map = HashMap(5)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))

#
# print("one: {}".format(hash_map.get("one")))
# print("neo: {}".format(hash_map.get("neo")))
# print("three: {}".format(hash_map.get("three")))
# print("size: {}".format(hash_map.size()))

hash_map.delete("one")
print("size: {}".format(hash_map.size()))
print("two: {}".format(hash_map.get("two")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("one: {}".format(hash_map.get("one")))

hash_map.delete("one")
hash_map                          # call to the helper function to see the hashmap

print(hash_map.get("one"))
print(hash_map.size())
print(hash_map)



