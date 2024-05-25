def divide_and_sort(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    """
    smaller on the left 
    and greater on the right
    """
    while i < j:
        # to find the first largest element which is greater than or equals to pivot
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        # to find the first element which is lesser than pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

"""
TC: N * log N
TC: O(n*log2(n))
SC: O(1)
"""
def quick_sort(arr, low, high):
    if low < high:
        partition = divide_and_sort(arr, low, high)
        quick_sort(arr, low, partition - 1)
        quick_sort(arr, partition + 1, high)
    return arr

arr = [1, 2, -1, -5, 0, 5, 4]
print(quick_sort(arr, 0, len(arr)-1))
