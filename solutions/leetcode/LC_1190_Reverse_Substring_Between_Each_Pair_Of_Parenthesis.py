# Solution for 1190 Reverse substring between each pair of parenthesis
# Platform: LeetCode
# Date: 2026-09-27
#
class Solution:
    def reverseParentheses(self, s: str) -> str:

        stk = []
        res = ""
        for ch in s:
            if ch == "(":
                stk.append(res)
                res = ""
            elif ch == ")":
                res = stk.pop() + res[::-1]
            else:
                res += ch
        return res
