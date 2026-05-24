# Solution for 1340. Jump Game V
# Platform: LeetCode
# Date: 2026-05-24
#

from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        seen = dict()
        n = len(arr)

        def _jump(i):
            if i in seen:
                return
            seen[i] = 1
            j = i - 1
            while j >= 0 and i - j <= d and arr[i] > arr[j]:
                _jump(i)
                seen[i] = max(seen[i], seen[j] + 1)
                j -= 1
            j = i + 1

            while j < n and j - i <= d and arr[i] > arr[j]:
                _jump(j)
                seen[i] = max(seen[i], seen[j] + 1)
                j += 1

        for i in range(n):
            _jump(i)

        return max(seen.values())
