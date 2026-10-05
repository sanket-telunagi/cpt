# Solution for 856 Score of Parentheses
# Platform: LeetCode
# Date: 2026-10-05
#


class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        score, depth = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1
                if s[i - 1] == "(":
                    score += 2**depth
        return score
