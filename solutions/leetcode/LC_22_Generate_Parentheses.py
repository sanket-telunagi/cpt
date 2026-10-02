# Solution for 22 Generate Parentheses
# Platform: LeetCode
# Date: 2026-10-02
#
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        path = []

        def generateTree(open, closed):

            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open < n:
                path.append("(")
                generateTree(open + 1, closed)
                path.pop()
            if closed < open:
                path.append(")")
                generateTree(open, closed + 1)
                path.pop()

        generateTree(0, 0)
        return res
