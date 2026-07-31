# Solution for 3016. Minimum Number of Pushes to Type Word II
# Platform: LeetCode
# Date: 2026-07-31
#
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for c in word :
            freq[ord(c) - ord('a')] += 1
        freq.sort(reverse=True)
        push = 0
        for i in range(26) :
            if freq[i] == 0 :
                break
            push += (i//8 + 1) * freq[i]
        return push
