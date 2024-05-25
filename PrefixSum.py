def sum_of_range(arr, l, r):
    prefix_sum = PrefixSum(arr)
    return prefix_sum[r+1] - prefix_sum[l]



def PrefixSum(arr):
    prefix_sum = [0]
    for i in range(len(arr)): prefix_sum.append(arr[i] + prefix_sum[i])
    return prefix_sum

n, q= map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]
for i in range(len(nums)): prefix_sum.append(nums[i] + prefix_sum[i])
for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l-1])