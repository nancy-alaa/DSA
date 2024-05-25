def maxSubArray(nums) -> int:
    # using Kadane's Algorithm
    """
    TC: O(N)
    SC: O(1)
    """
    summation, max_subarray_sum = 0, nums[0]
    for num in nums:
        summation += num
        max_subarray_sum = max(max_subarray_sum, summation)
        summation = max(summation, 0)
    return max_subarray_sum
