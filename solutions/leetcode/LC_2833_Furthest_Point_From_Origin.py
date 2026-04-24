# Solution for 2833. Furthest Point From Origin
# Platform: LeetCode
# Date: 2026-04-24
#

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r1, r2 = 0, 0
        hash = {
            "L" : -1,
            "R" : 1
        }
        for move in moves : 
            if move == "_" :
                r1 += hash['L']
                r2 += hash['R']
            
            else : 
                r2 += hash[move]
                r1 += hash[move]

        return max(abs(r1), abs(r2))
