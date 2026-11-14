# Solution for 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Platform: LeetCode
# Date: 2026-11-12
#


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_increasing = 1
        longest_increasing_curr = 1
        longest_decreasing = 1
        longest_decreasing_curr = 1

        i = 0 
        n = len(nums)
        for i in range(n -1) :
            if nums[i+1] > nums[i] and nums[i+1] - nums[i] >= 1:
                longest_increasing_curr += 1
            else : 
                longest_increasing_curr = 1
            
            if nums[i+1] < nums[i] and nums[i+1] - nums[i] <= -1 :
                longest_decreasing_curr += 1
            else :
                longest_decreasing_curr = 1
            
            longest_increasing = max(longest_increasing, longest_increasing_curr)
            longest_decreasing = max(longest_decreasing, longest_decreasing_curr)

        return max(longest_increasing, longest_decreasing)
        
        
