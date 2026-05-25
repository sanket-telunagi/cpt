# Solution for 1871. Jump Game VII
# Platform: LeetCode
# Date: 2026-05-25
#


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, prefix = [0] * n, [0] * n
        f[0] = 1
        for i in range(minJump):
            prefix[i] = 1
        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = prefix[right] - (0 if left <= 0 else prefix[left - 1])
                f[i] = int(total != 0)
            prefix[i] = prefix[i - 1] + f[i]

        return bool(f[n - 1])
