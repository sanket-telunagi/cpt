# Solution for 836 Rectangle Overlap
# Platform: LeetCode
# Date: 2026-09-14
#
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        if x1 == x2 or y1 == y2 or x3 == x4 or y3 == y4:
            return False

            return not (x2 <= x3 or x1 >= x4 or y2 <= y3 or y1 >= y4)
