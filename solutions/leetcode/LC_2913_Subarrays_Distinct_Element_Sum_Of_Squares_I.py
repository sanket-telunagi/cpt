# Solution for 2913. Subarrays Distinct Element Sum of Squares I
# Platform: LeetCode
# Date: 2026-10-15
#


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                res += len(set(nums[i:j])) ** 2
        return res


class Solution2:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        i, j = 0, 0

        for _ in range(total_subarrays):
            res += len(set(nums[i : j + 1])) ** 2
            j += 1
            if j == n:
                i += 1
                j = i
        return res
