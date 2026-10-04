# Solution for 678 Valid Parenthesss String
# Platform: LeetCode
# Date: 2026-10-04
#


class Solution:
    def checkValidString(self, s: str) -> bool:
        ct = {"(": [], "*": []}

        for i, ch in enumerate(s):
            if ch == "(":
                ct["("].append(i)
            elif ch == "*":
                ct["*"].append(i)
            elif ch == ")":
                if ct["("]:
                    ct["("].pop()
                elif ct["*"]:
                    ct["*"].pop()
                else:
                    return False

        while ct["("] and ct["*"]:
            if ct["("][-1] < ct["*"][-1]:
                ct["("].pop()
                ct["*"].pop()
            else:
                return False

        return len(ct["("]) == 0
