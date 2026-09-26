# Solution for 1807 Evaluate Bracket Pairs of a String
# Platform: LeetCode
# Date: 2026-09-26
#
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        for k, v in knowledge:
            s = s.replace(f"({k})", v)

        keys = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                i += 1
                temp = ""
                while s[i] != ")":
                    temp += s[i]
                    i += 1
                keys.append(f"({temp})")
            else:
                i += 1
        # print(keys)
        for k in keys:
            s = s.replace(k, "?")

        return s


class Solution2:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        GK = {}
        for k, v in knowledge:
            GK[k] = v

        keys = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                i += 1
                temp = ""
                while s[i] != ")":
                    temp += s[i]
                    i += 1
                keys.append(temp)
            else:
                i += 1
        for k in keys:
            s = s.replace(f"({k})", GK.get(k, "?"))

        return s


class Solution3:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        GK = {}
        for k, v in knowledge:
            GK[k] = v

        res = ""
        i = 0
        while i < len(s):
            if s[i] == "(":
                i += 1
                temp = ""
                while s[i] != ")":
                    temp += s[i]
                    i += 1
                res += GK.get(temp, "?")
                i += 1
            else:
                res += s[i]
                i += 1

        return res
