# Solution for 2126. Destroying Asteroids
# Platform: LeetCode
# Date: 2026-05-31
#
#
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, nums: List[int]) -> bool:
        M = max(nums)
        while nums:
            seen = []
            for num in nums:
                if num > mass:
                    seen.append(num)
                else:
                    mass += num
                    if mass >= M:
                        return True
            if len(nums) == len(seen):
                return False
            nums = seen
        return False


class Solution2:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for num in asteroids:
            if num > mass:
                return False
            mass += num
        return True
