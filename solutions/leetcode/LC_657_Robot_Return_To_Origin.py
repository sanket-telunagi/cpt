# Solution for 657. Robot Return to Origin
# Platform: LeetCode
# Date: 2026-04-06
#


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mp = {"U": 1, "D": -1, "L": 1, "R": -1}
        x, y = 0, 0
        for ch in moves:
            if ch == "U" or ch == "D":
                y += mp[ch]
            else:
                x += mp[ch]

        return x == y == 0
