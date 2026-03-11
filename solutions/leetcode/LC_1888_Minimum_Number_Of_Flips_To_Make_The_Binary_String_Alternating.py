# Solution for 1888. Minimum Number of Flips to Make the Binary String Alternating
# Platform: LeetCode
# Date: 2026-03-07
#

s = input()

ct = 0
# move in window of two
for i in range(len(s) - 1):
    curr = s[i]
    next = s[i + 1]
    if curr == next:
        ct += 1

print(ct // 2)
