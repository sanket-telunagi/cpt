# Solution for 3761. Minimum Absolute Distance Between Mirror Pairs
# Platform: LeetCode
# Date: 2026-04-17
#

from typing import List

# solution one : bruteforce

# class Solution:
#     def minMirrorPairDistance(self, nums: List[int]) -> int:
#         HIGH = 10**7 + 7
#         res = HIGH
#         n = len(nums)

#         def reverse_digits(val):
#             res = 0
#             while val > 0:
#                 last = val % 10
#                 res = res * 10 + last
#                 val //= 10
#             return res

#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if i != j and (i < n - 1) and (j >= (i + 1)):
#                     # print(i, j, num1, num2, reverse_digits(num1), reverse_digits(num2))
#                     if reverse_digits(num1) == num2:
#                         res = min(res, abs(i - j))

#         return res if res < HIGH else -1
