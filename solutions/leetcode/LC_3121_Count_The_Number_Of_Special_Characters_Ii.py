# Solution for 3121. Count the Number of Special Characters II
# Platform: LeetCode
# Date: 2026-05-27
#
#
# version : v1
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        first_upper_case = {}
        lower = {}

        for idx, ch in enumerate(word):
            if ch.isupper():
                if ch not in first_upper_case:
                    first_upper_case[ch] = idx
            if ch.islower():
                if ch in lower:
                    lower[ch].append(idx)
                else:
                    lower[ch] = [idx]
        count = 0
        for ch, occur in lower.items():
            if (
                ch.upper() in first_upper_case
                and occur[-1] < first_upper_case[ch.upper()]
            ):
                count += 1

        return count


# version v2
class Solution2:
    def numberOfSpecialChars(self, word: str) -> int:

        hash = {}

        for idx, ch in enumerate(word):
            if ch.isupper():
                if hash.get(ch) is None:
                    hash[ch] = idx
            else:
                hash[ch] = idx

        count = 0
        for ch, occur in hash.items():
            if ch.islower():
                if (hash.get(ch.upper(), None) is not None) and occur < hash[
                    ch.upper()
                ]:
                    count += 1

        return count
