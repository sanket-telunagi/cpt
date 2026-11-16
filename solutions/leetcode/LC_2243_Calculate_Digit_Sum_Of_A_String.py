# Solution for 2243. Calculate Digit Sum of a String
# Platform: LeetCode
# Date: 2026-11-16
#

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        temp = []
        while n > k : 
            for i in range(0, n, k) :
                substr = s[i:i+k]
                addition = sum(list(map(int, substr)))
                temp.append(str(addition))
            s = "".join(temp)
            temp = []
            n = len(s)

        return s
