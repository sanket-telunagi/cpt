# Solution for 20 Valid Parenthesis
# Platform: LeetCode
# Date: 2026-10-01
#


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stk = []
        n = len(s)

        for ch in range(n):
            if s[ch] in mapping:
                if not stk or stk.pop() != mapping[s[ch]]:
                    return False
            else:
                stk.append(s[ch])
        return not stk
