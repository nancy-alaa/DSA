def merge(arr, low, mid, high):
    temp_arr = []

    # we keep two pointers left, right to compare
    left = low
    right = mid + 1

    # then we compare
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left += 1
        else:
            temp_arr.append(arr[right])
            right += 1
    while left <= mid:
        temp_arr.append(arr[left])
        left += 1
    while right <= high:
        temp_arr.append(arr[right])
        right += 1

    # copying the temp to the original array
    for i in range(low, high + 1):
        arr[i] = temp_arr[i - low]

"""
It has a Time Complexity of
O(log2(n))
The worst case for merge function is O(n)
the the merge_sort has n * log2(n)
"""
def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

arr = [2, 5, -1, 0, 1, 9, 14]
merge_sort(arr, 0, len(arr)-1)
print(arr)























