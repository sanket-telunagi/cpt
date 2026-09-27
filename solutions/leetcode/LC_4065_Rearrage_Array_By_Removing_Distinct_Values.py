# Solution for 4065 Rearrage array by removing distinct values
# Platform: LeetCode
# Date: 2026-09-27
#
#


class Solution1:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        h = dict(sorted(h.items()))
        ans = []
        while sum(h.values()) != 0:
            for k, v in h.items():
                if v == 0:
                    continue
                elif v > 0:
                    ans.append(k)
                    h[k] -= 1
        return ans


class Solution2:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        ans = []
        while h:
            for k in sorted(h.keys()):
                ans.append(k)
                h[k] -= 1
                if h[k] == 0:
                    del h[k]
        return ans
