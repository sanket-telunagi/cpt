# Solution for Minimise maximum pair sum in an array
# Platform: LeetCode
# Date: 2026-01-24
#

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # works but lets try without sorting
        nums.sort()

        pair_sum = []

        for i in range(len(nums) // 2):
            pair_sum.append((nums[i] + nums[-(i + 1)]))

        return max(pair_sum)


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().minPairSum(nums))
