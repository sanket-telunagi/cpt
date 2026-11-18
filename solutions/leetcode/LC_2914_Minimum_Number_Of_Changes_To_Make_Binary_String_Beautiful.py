# Solution for 2914. Minimum Number of Changes to Make Binary String Beautiful
# Platform: LeetCode
# Date: 2026-11-18
#
# approach : 
#     the minimum changes can be found in the smallest chunk, if the smallest chunk is right every substring will be correct 
#     smallest chunk will be of 2 chars, if no same we will need to change it

class Solution:
    def minChanges(self, s: str) -> int:
        res = 0 
        for i in range(0, len(s), 2) :
            res += 1 if s[i] != s[i+1] else 0
        return res

class Solution2:
    def minChanges(self, s: str) -> int:
        return sum([1 if s[i] != s[i+1] else 0 for i in range(0, len(s), 2)])
