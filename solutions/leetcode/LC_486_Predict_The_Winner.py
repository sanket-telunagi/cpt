# Solution for 486 Predict The Winner
# Platform: LeetCode
# Date: 2026-08-01
#
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 == 0 : return True
        dp = nums.copy()
        for i in range(n-2, -1, -1) :
            for j in range(i + 1, n) :
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])

        return dp[-1] >= 0
