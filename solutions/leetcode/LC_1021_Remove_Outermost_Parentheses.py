# Solution for 1021 Remove Outermost Parentheses
# Platform: LeetCode
# Date: 2026-10-08
#


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        nesting = 0

        for ch in s:
            if ch == ")":
                nesting -= 1
            if nesting > 0:
                res = res + ch
            if ch == "(":
                nesting += 1

        return res
