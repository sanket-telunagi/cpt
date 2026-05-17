# Solution for 1306. Jump Game III
# Platform: LeetCode
# Date: 2026-05-17
#
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        n = len(arr)

        def _rec(i):
            if i < 0 or i >= n or i in seen:
                return False
            if arr[i] == 0:
                return True
            seen.add(i)

            return _rec(i + arr[i]) or _rec(i - arr[i])

        return _rec(start)


class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def _rec(i):

            if i < 0 or i >= n or arr[i] == -1:
                return False
            if arr[i] == 0:
                return True
            jump = arr[i]
            arr[i] = -1

            return _rec(i + jump) or _rec(i - jump)

        return _rec(start)
