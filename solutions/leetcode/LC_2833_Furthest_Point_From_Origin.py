# Solution for 2833. Furthest Point From Origin
# Platform: LeetCode
# Date: 2026-04-24
#


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r1, r2 = 0, 0
        hash = {"L": -1, "R": 1}
        for move in moves:
            if move == "_":
                r1 += hash["L"]
                r2 += hash["R"]

            else:
                r2 += hash[move]
                r1 += hash[move]

        return max(abs(r1), abs(r2))


# beats 100% cpu 98% memory
class Solution2:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        h = {"R": 0, "L": 0, "_": 0}
        for m in moves:
            h[m] += 1
        return abs(h["R"] - h["L"]) + h["_"]
