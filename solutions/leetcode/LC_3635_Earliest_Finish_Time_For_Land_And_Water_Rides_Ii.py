# Solution for 3635. Earliest Finish Time for Land and Water Rides II
# Platform: LeetCode
# Date: 2026-06-03
#
from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:

        def _(s1, s2, d1, d2):
            f1 = 1000_000_0000_000
            for i in range(len(s1)):
                f1 = min(f1, s1[i] + d1[i])

            f2 = 1000_000_0000_000
            for i in range(len(s2)):
                f2 = min(f2, max(s2[i], f1) + d2[i])

            return f2

        lw = _(landStartTime, waterStartTime, landDuration, waterDuration)
        wl = _(waterStartTime, landStartTime, waterDuration, landDuration)

        return min(lw, wl)
