# Solution for 3498 Reverse Degree of A String
# Platform: LeetCode
# Date: 2026-09-20
#


class Solution:
    def reverseDegree(self, s: str) -> int:
        hash = {
            "a": 26,
            "b": 25,
            "c": 24,
            "d": 23,
            "e": 22,
            "f": 21,
            "g": 20,
            "h": 19,
            "i": 18,
            "j": 17,
            "k": 16,
            "l": 15,
            "m": 14,
            "n": 13,
            "o": 12,
            "p": 11,
            "q": 10,
            "r": 9,
            "s": 8,
            "t": 7,
            "u": 6,
            "v": 5,
            "w": 4,
            "x": 3,
            "y": 2,
            "z": 1,
        }
        res = 0
        i = 0
        for ch in s:
            res += hash[ch] * (i + 1)
            i += 1
        return res


class Solution2:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, s in enumerate(s):
            res += (ord("a") - ord(s) + 26) * (i + 1)
        return res
