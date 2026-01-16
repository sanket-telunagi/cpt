# Solution for CF_1955A_Yogurt_Sale
# Platform: CodeForces
# Date: 2026-01-16
#

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    val = (n // 2 * b) + (n % 2 * a)
    print(min(n * a, val))
