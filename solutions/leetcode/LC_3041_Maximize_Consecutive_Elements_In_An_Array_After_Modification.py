# Solution for 3041. Maximize Consecutive Elements in an Array After Modification
# Platform: LeetCode
# Date: 2026-11-20
#

class Solution:

    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        
        prev = nums[0]
        keep = 1  
        inc = 1   
        res = 1
        
        for x in nums[1:]:
            if x == prev:
                inc = keep + 1
            elif x == prev + 1:
                keep += 1
                inc += 1
                prev = x
            elif x == prev + 2:
                keep = inc + 1
                inc = 1
                prev = x
            else:
                keep = 1
                inc = 1
                prev = x
            
            res = max(res, keep, inc)
            
        return res
