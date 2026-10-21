# Solution for 3863. Minimum Operations to Sort a String
# Platform: LeetCode
# Date: 2026-10-21
#


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        maximum, minimum = max(s), min(s)
        if all(a <= b for a, b in zip(s,s[1:])) :
            return 0
        if n == 2 :
            return -1
        if s[0] == minimum or s[-1] == maximum :
            return 1
        for i in range(1, n-1) :
            if s[i] == minimum or s[i] == maximum :
                return 2
        return 3
