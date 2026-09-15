# Solution for 2472 Maximum Number of Non-Overlapping Palindrome Substrings
# Platform: LeetCode
# Date: 2026-09-15
#


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        def isPal(subs):
            return subs == subs[::-1]

        n = len(s)
        res = 0
        start = 0
        for r in range(k - 1, n):
            l = r - k + 1
            if l >= start and isPal(s[l : r + 1]):
                res += 1
                start = r + 1
                continue
            l = r - k
            if l >= start and isPal(s[l : r + 1]):
                res += 1
                start = r + 1
        return res
