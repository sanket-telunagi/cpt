# Solution for 3411 Maximum Subarray With Equal Products
# Platform: LeetCode
# Date: 2026-11-24
#

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        import math
        n = len(nums)
        res = 0
        for i in range(n) :
            for j in range(i+1, n) :
                temp = nums[i : j+1]
                if math.prod(temp) == math.gcd(*temp) * math.lcm(*temp) :
                    res = max(res, j - i + 1)
        return res
        
class Solution2:
    def maxLength(self, nums: List[int]) -> int:
        from math import prod, gcd, lcm
        n = len(nums)
        res = 0
        for i in range(n) :
            for j in range(i+1, n) :
                temp = nums[i : j+1]
                if prod(temp) == gcd(*temp) * lcm(*temp) :
                    res = max(res, j - i + 1)
        return res
