# Solution for 921. Minimum Add to Make Parentheses Valid
# Platform: LeetCode
# Date: 2026-10-13
#
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_ct, adds = 0, 0
        for ch in s:
            if ch == "(":
                open_ct += 1
            else:
                if open_ct > 0:
                    open_ct -= 1
                else:
                    adds += 1
        return open_ct + adds
