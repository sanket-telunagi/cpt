# Solution for 3120. Count the Number of Special Characters I
# Platform: LeetCode
# Date: 2026-05-26
#

# approach 1
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hash = set(list(word))
        hash2 = [False] * 26
        count = 0
        for i in word:
            if not hash2[ord("a") - ord(i.lower())]:
                if i.isupper():
                    if i.lower() in hash:
                        count += 1
                else:
                    if i.upper() in hash:
                        count += 1
                hash2[ord("a") - ord(i.lower())] = True

        return count
