# Solution for 1401 Circle and Rectangle Overlapping
# Platform: LeetCode
# Date: 2026-09-19
#


class Solution:
    def checkOverlap(
        self, r: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int
    ) -> bool:

        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y

        return (dist_x**2 + dist_y**2) <= (r**2)
