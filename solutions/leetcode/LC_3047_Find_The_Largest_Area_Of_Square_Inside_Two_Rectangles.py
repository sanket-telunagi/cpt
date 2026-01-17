# Solution for LC_3047_Find_The_Largest_Area_Of_Square_Inside_Two_Rectangles
# Platform: LeetCode
# Date: 2026-01-17
#

from Typing import List
from itertools import combinations


class Solution:
    def largestSquareArea(self, bl: List[List[int]], tr: List[List[int]]) -> int:
        max_res = 0

        for (bli, tri), (blj, trj) in combinations(zip(bl, tr), 2):
            w = min(tri[0], trj[0]) - max(bli[0], blj[0])
            h = min(tri[1], trj[1]) - max(bli[1], blj[1])
            max_res = max(max_res, min(w, h))

        return max_res**2
