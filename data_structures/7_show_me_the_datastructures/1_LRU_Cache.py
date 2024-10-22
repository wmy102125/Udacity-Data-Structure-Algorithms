from collections import deque, defaultdict


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

## Test Case 2
our_cache.set('name6', 'wmy6');

test_case_2 = ["name6","wmy6"]
test_fuciont_get(test_case_2,our_cache)
test_case_2 = ["name1",-1]
test_fuciont_get(test_case_2,our_cache)
## Test Case 3
output  = {'name3': 'wmy3', 'name4': 'wmy4', 'name5': 'wmy5', 'name6': 'wmy6', 'name7': 'wmy7'}
test_case_3 = ["name7",output]
