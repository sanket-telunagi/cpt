# Solution for 32 Longest Valid Parentheses
# Platform: LeetCode
# Date: 2026-10-03
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        res = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


class Solution2:
    def longestValidParentheses(self, s: str) -> int:

        open_ct, close_ct, res = 0, 0, 0

        for c in s:
            if c == "(":
                open_ct += 1
            else:
                close_ct += 1

            if open_ct == close_ct:
                res = max(res, 2 * close_ct)

            if close_ct > open_ct:
                open_ct, close_ct = 0, 0

        open_ct, close_ct = 0, 0

        for c in reversed(s):
            if c == "(":
                open_ct += 1
            else:
                close_ct += 1
            if open_ct == close_ct:
                res = max(res, 2 * close_ct)

            if open_ct > close_ct:
                open_ct = close_ct = 0
        return res
