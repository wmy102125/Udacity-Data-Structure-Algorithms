import collections

# Define Item as a named tuple
Item = collections.namedtuple('Item', ['weight', 'value'])


# Naive Approach based on Recursion
def knapsack_max_value(knapsack_max_weight, items):
    lastIndex = len(items) - 1
    return knapsack_recursive(knapsack_max_weight, items, lastIndex)


def knapsack_recursive(capacity, items, lastIndex):
    print(f"Entering: Capacity = {capacity}, LastIndex = {lastIndex}")

    # Base case
    if (capacity <= 0) or (lastIndex < 0):
        print(f"Base case hit: Returning 0 for Capacity = {capacity}, LastIndex = {lastIndex}")
        return 0

    # Put the item in the knapsack
    valueA = 0
    if (items[lastIndex].weight <= capacity):
        valueA = items[lastIndex].value + knapsack_recursive(capacity - items[lastIndex].weight, items, lastIndex - 1)

    # Do not put the item in the knapsack
    valueB = knapsack_recursive(capacity, items, lastIndex - 1)

    # Pick the maximum of the two results
    result = max(valueA, valueB)

    print(f"Returning: Capacity = {capacity}, LastIndex = {lastIndex}, Result = {result}")
    return result


# Test
tests = [
    {
        'correct_output': 14,
        'input': {
            'knapsack_max_weight': 15,
            'items': [Item(10, 7), Item(9, 8), Item(5, 6)]
        }
    }
]

for test in tests:
    print("\nStarting new test case")
    output = knapsack_max_value(**test['input'])
    assert output == test['correct_output'], f"Test failed: Expected {test['correct_output']}, got {output}"
    print("Test passed.")

"""
The Approach - Dynamic Programming
Store and reuse the intermediate results in a lookup table. This step is called memoization. Start with initializing a lookup table (a list), where the index represents the remaining capacity (kg) of the knapsack, and the element represents the maximum value ( $
 ) that it can hold.

For a given item, if the item-weight is less than the remaining capacity (kg) of the knapsack, then we have two options:

Do not pick the item - In this case, the value ( $
 ) of knapsack with the remaining capacity would not change. It can be represented as lookup_table[capacity].
Pick the item - In this case, the value ( $
 ) and capacity (kg) of the knapsack would be updated. The value ( $
 ) of the knapsack will be equal to value ( $
 ) of the current object + value ( $
 ) in the lookup table at [capacity - item.weight] position. It can be represented as lookup_table[capacity - item.weight] + item.value.
Update the lookup table, lookup_table[capacity], with the maximum of either of the above two values.

Note - This approach with dynamic programming will have a time complexity as  𝑂(2𝑛𝐶)≡𝑂(𝑛𝐶)
 , where  𝑛
  is the number of given items and  𝐶
  is the max capacity (kg) of the knapsack.
"""


def knapsack_max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    lookup_table = [0 for _ in range(0, knapsack_max_weight + 1)]
    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight]+item.value)
            else:
                break
    return lookup_table[-1]


# solution
# DP Solution
# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value_solution(knapsack_max_weight, items):
    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:

        # The "capcacity" represents amount of remaining capacity (kg) of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):

            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)
            else:
                break

    return lookup_table[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
