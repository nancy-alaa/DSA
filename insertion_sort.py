"""
Time Complexity: O(n^2)
best case is O(n)
"""
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

print(insertion_sort([2, 13, 4, 1, 3, 6, 28, 0]))

