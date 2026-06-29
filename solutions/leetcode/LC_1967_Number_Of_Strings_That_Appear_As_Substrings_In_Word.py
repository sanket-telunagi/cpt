# Solution for 1967. Number of Strings That Appear as Substrings in Word
# Platform: LeetCode
# Date: 2026-06-29
#

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for s in patterns:
            if word.__contains__(s):
                res += 1
        return res
