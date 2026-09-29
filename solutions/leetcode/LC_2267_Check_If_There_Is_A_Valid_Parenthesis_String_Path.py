# Solution for 2267 Check if there is a valid parenthesis string path
# Platform: LeetCode
# Date: 2026-09-29
#
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0 or grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        dp = [0] * n

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    prev = 1
                else:
                    prev = (dp[c] if r > 0 else 0) | (dp[c - 1] if c > 0 else 0)

                if grid[r][c] == "(":
                    dp[c] = prev << 1
                else:
                    dp[c] = prev >> 1

        return bool(dp[-1] & 1)


class Solution2:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        visited = set()
        stk = []

        def travel(i: int, j: int) -> bool:
            state = (i, j, len(stk))
            if state in visited:
                return False

            char = grid[i][j]
            popped = False

            if stk and stk[-1] == "(" and char == ")":
                stk.pop()
                popped = True
            else:
                stk.append(char)

            if not popped and char == ")":
                stk.pop()
                return False

            if i == m - 1 and j == n - 1:
                is_valid = len(stk) == 0
                if popped:
                    stk.append("(")
                else:
                    stk.pop()
                return is_valid

            found = False
            if i + 1 < m and travel(i + 1, j):
                found = True
            elif j + 1 < n and travel(i, j + 1):
                found = True

            if popped:
                stk.append("(")
            else:
                stk.pop()

            if not found:
                visited.add(state)

            return found

        return travel(0, 0)
