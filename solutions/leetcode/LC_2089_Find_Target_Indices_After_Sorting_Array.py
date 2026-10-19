# Solution for 2089. Find Target Indices After Sorting Array
# Platform: LeetCode
# Date: 2026-10-19
#


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums.sort()
        for i, num in enumerate(nums) :
            if num == target :
                res.append(i)

        return res
