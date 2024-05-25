"""
Time Complexity For Selection Sort:
      n + n-1 + n-2 + n-3 + ....
      n * (n+1)/2 which is
      the summation of the first n natural numbers
      ==
      n^2 + n/2
    Time Complexity = O(n^2)
"""
def selection_sort(nums):
    for i in range(len(nums)-1):
        mini_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[mini_idx]:
                mini_idx = j
        nums[i], nums[mini_idx] = nums[mini_idx], nums[i]
    return nums
print(selection_sort([2, 13, 4, 1, 3, 6, 28]))



