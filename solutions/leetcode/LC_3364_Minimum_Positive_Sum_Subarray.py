# Solution for 3364. Minimum Positive Sum Subarray
# Platform: LeetCode
# Date: 2026-11-14
#

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = 10_00_00_00_00

        for i in range(n) :
            for j in range(i, n) :
                # print(nums[i:j+1])
                if (j-i +1) >= l and (j-i+1) <= r :
                    # print(nums[i: j+1])
                    _ = sum(nums[i:j+1])
                    if _ > 0 :
                        res = min(res, _)
        return -1 if res >= 10_00_00_00 else res
