# Basic Recursion Problems
import math


# 1. Print Name 5 times
def print_name(i, n, name):
    if i > n:
        return
    print(name)
    print_name(i+1, n, name)
# print_name(1, 5, "name")


# 2. Print Linearly From 1 to N
def print_nums_from_i_to_n(i, n):
    if i > n:
        return
    print(i)
    print_nums_from_i_to_n(i+1, n)
# print_nums_from_i_to_n(1, 5)

# 3. Print In Terms Of N to 1
def print_nums_from_n_to_i(n, i):
    if n < i:
        return
    print(n)
    print_nums_from_n_to_i(n-1, i)
# print_nums_from_n_to_i(5, 3)

# 4. Print From 1 to N using Backtracking
def print_from1toN_backtracking(n):
    if n < 1:
        return
    print_from1toN_backtracking(n-1)
    print(n)
# print_from1toN_backtracking(4)


# 5. Print From N to 1 using Backtracking
def print_fromNto1_backtracking(i, n):
    if i > n:
        return
    print_fromNto1_backtracking(i+1, n)
    print(i)
# print_fromNto1_backtracking(1, 5)

# def print_fromNto1_backtracking(n):
#     if n < 1:
#         return
#     print(n)
#     return print_fromNto1_backtracking(n-1)
# print_fromNto1_backtracking(4)


def summation_of_first_n_numbers(n):
    if n == 0: return 0
    return n + summation_of_first_n_numbers(n-1)

# print(summation_of_first_n_numbers(5))

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
# print(factorial(5))

arr = [1, 2, 3, 4, 5]
def reverse_arr(l, r, arr):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse_arr(l+1, r-1, arr)
    return arr
# print(reverse_arr(0, 4, arr))

def reverseArray(n, nums, i = 0) :
    # Write your code here
    if i >= n // 2:
        return
    # swapping
    nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
    reverseArray(n, nums, i+1)
    return nums
# print(reverseArray(5, [1, 2, 3, 4, 5]))


def is_palindrome(string, i=0):
    if i >= len(string) // 2:
        return True
    if string[i] != string[len(string)-i-1]:
        return False
    return is_palindrome(string, i + 1)

# print(is_palindrome("abbba"))

def nth_fibonacci(n):
    if n == 0 or n == 1:
        return n
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)
# print(nth_fibonacci(4))
