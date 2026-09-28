# Solution for 1614 Maximum nesting depth of the Parenthesis
# Platform: LeetCode
# Date: 2026-09-28
#


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curr = 0
        for ch in s:
            if ch == "(":
                curr += 1
            elif ch == ")":
                curr -= 1
            else:
                continue
            res = max(res, curr)

        return res
