from collections import deque, defaultdict

"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_queue = deque(maxlen=capacity)
        self.cache_dict = dict()
        self.size = 0
        self.max_size = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache_dict is None:
            return -1
        if key in self.cache_dict:
            return self.cache_dict[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.size < self.max_size:
            self.cache_queue.appendleft(key)
            self.cache_dict[key] = value
            self.size += 1
            return
        else:
            old_key = self.cache_queue.pop()
            self.cache_dict.pop(old_key)
            self.cache_dict[key] = value
            self.cache_queue.appendleft(key)


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values
our_cache = LRU_Cache(5)

our_cache.set('name1', 'wmy1');
our_cache.set('name2', 'wmy2');
our_cache.set('name3', 'wmy3');
our_cache.set('name4', 'wmy4');
our_cache.set('name5', 'wmy5');

def test_fuciont_get(test_case,our_cache):
    output = our_cache.get(test_case[0])
    if test_case[1] == output:
        print("Pass")
    else:
        print("Fail")
def test_fuciont_set(test_case,our_cache):
    our_cache.set(test_case[0])
    if our_cache.cache_dict == test_case[1]:
        print("Pass")
    else:
        print("Fail")
## Test Case 1
test_case_1 = ["name1","wmy1"]
test_fuciont_get(test_case_1,our_cache)

## Test Case 2,getting the same value 6 times
our_cache.set('name6', 'wmy6');

test_case_2 = ["name6","wmy6"]
test_fuciont_get(test_case_2,our_cache)
test_fuciont_get(test_case_2,our_cache)
test_fuciont_get(test_case_2,our_cache)
test_fuciont_get(test_case_2,our_cache)
test_fuciont_get(test_case_2,our_cache)
test_fuciont_get(test_case_2,our_cache)
## Test Case 3,getting the invalid value
test_case_2 = ["name1",-1]
test_fuciont_get(test_case_2,our_cache)
## Test Case 4,set the None value
our_cache.set(None, None);

test_case_2 = [None,None]
test_fuciont_get(test_case_2,our_cache)

our_cache.set("namename", "valuevalue");
test_case_2 = ["namename","valuevalue"]
test_fuciont_get(test_case_2,our_cache)
