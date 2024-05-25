def majorityElement(nums) -> int:
    """
    TC: O(N)
    SC: O(1)
    """
    # using Moore's Voting algorithm
    element = nums[0]
    counter = 0
    for num in nums:
        if counter == 0: element = num
        if num == element:
            counter += 1
        else:
            counter -= 1
    return element