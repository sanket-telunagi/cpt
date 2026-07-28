# Solution for smallest-palindromic-rearrangement-i
# Platform: LeetCode
# Date: 2026-07-28
#

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        string_length = len(s)
        mid_index = string_length // 2
        first_half = s[:mid_index]
        sorted_chars = sorted(first_half)
        processed_half = "".join(sorted_chars)
        middle_char = s[mid_index]
        has_middle = string_length % 2
        center_piece = middle_char * has_middle
        reversed_half = processed_half[::-1]
        result = processed_half + center_piece + reversed_half
        return result
