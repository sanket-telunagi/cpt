# Solution for CF-1374 Required Number
# Platform: codeforces
# Date: 2026-01-24
#

for _ in range(int(input())):
    x, y, n = map(int, input().split())

    print(((n - y) // x) * x + y)
