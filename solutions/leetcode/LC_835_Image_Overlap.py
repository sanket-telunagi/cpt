# Solution for 835 Image Overlap
# Platform: LeetCode
# Date: 2026-09-13
#
from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        def count_overlap(shift_x: int, shift_y: int) -> int:
            overlap = 0
            for r in range(n):
                for c in range(n):
                    img2_r = r + shift_y
                    img2_c = c + shift_x

                    if 0 <= img2_r < n and 0 <= img2_c < n:
                        if img1[r][c] == 1 and img2[img2_r][img2_c] == 1:
                            overlap += 1
            return overlap

        for y in range(-(n - 1), n):
            for x in range(-(n - 1), n):
                max_overlap = max(max_overlap, count_overlap(x, y))
        return 1


class Solution2:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        def count_overlap(shift_x: int, shift_y: int) -> int:
            overlap = 0
            for r in range(n):
                for c in range(n):
                    img2_r = r + shift_y
                    img2_c = c + shift_x

                    if 0 <= img2_r < n and 0 <= img2_c < n:
                        if img1[r][c] and img2[img2_r][img2_c]:
                            overlap += 1
            return overlap

        for y in range(-(n - 1), n):
            for x in range(-(n - 1), n):
                max_overlap = max(max_overlap, count_overlap(x, y))
        return max_overlap


class Solution3:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        vector_counts = Counter()
        max_overlap = 0

        for r1, c1 in list1:
            for r2, c2 in list2:
                vector = (r2 - r1, c2 - c1)
                vector_counts[vector] += 1
                max_overlap = max(max_overlap, vector_counts[vector])

        return max_overlap
