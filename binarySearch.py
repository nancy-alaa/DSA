# Test Location
# it takes a specific position and tell if this position is the answer
# to handle cases like [8, 8, 6, 6, 6, 6, 1, 0] and we are looking for 6
# & it should return the first occurrence of the query
# Those functions works correctly if the nums are sorted in decreasing order
# swap the left and right in the locate_function if the nums are sorted in increasing order

def test_location(nums, query, mid_idx):
    mid_number = nums[mid_idx]
    if mid_number == query:
        if mid_idx - 1 >= 0 and nums[mid_idx - 1] == query: return 'left'
        else: return 'found'
    elif mid_number < query: return 'left'
    else: return 'right'


# Binary Search
def binary_search(nums, query):
    nums.sort(reverse=True)
    first, last = 0, len(nums) - 1

    while first <= last:
        mid_idx = (first + last) // 2
        result = test_location(nums, query, mid_idx)

        if result == 'found': return mid_idx
        elif result == 'left': last = mid_idx - 1
        elif result == 'right': first = mid_idx + 1

    return -1

print(binary_search([13, 11, 10, 7, 4, 3, 1, 0], 7))

#Testing
large_test = {
    'input': {
        'nums': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

print(binary_search(**large_test['input']))
"""
Analyze the algorithm's complexity and identify inefficiencies if any?

Initial length: N
Iteration 1 - N/2
Iteration 2 - N/4 == N/2^2
Iteration 3- N/8 == N/2^3
.
.
Iteration k - N/2^k

since the final length of the array is 1, we can find the
N/2^k = 1

Rearranging the terms, we get
N = 2^k

Taking the logarithm

k = log N 

log to the base 2

Then, Binary Search has 
Time Complexity of: O(log N)
Space Complexity: O(1)
"""

# Generic Binary Search (given a range)
def generic_binary_search(first, last, condition):
    """docs"""
    while first <= last:
        mid_idx = (first + last) // 2
        result = condition(mid_idx)
        if result == 'found': return mid_idx
        elif result == 'left': last = mid_idx - 1
        else: first = mid_idx + 1
    return -1