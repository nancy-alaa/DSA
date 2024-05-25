"""
Bubble Sort is the opposite to the selection sort
it pushes the maximum to the last index

Its Time Complexity is the same as selection sort which is nearly
Time Complexity: ~ O(n^2)
Best Case if the array is sorted: Time Complexity: O(n)
"""

def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        swapped = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not swapped:
            break
    return nums
print(bubble_sort([2, 13, 4, -1, 3, 6, 28, 0]))



