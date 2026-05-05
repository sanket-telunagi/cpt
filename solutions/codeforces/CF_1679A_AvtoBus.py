# Solution for 1679 AVTOBUS
# Platform: CodeForces
# Date: 2026-05-05
#


def solve():
    n = int(input())
    if n % 2 != 0 or n < 4:
        print(-1)
        return

    x = n // 6

    if n % 6 != 0:
        x += 1
    y = n // 4

    print(f"{x} {y}")

    # print(*[n // 6 + 1 if n % 6 != 0 else n // 6, n // 4])


_ = int(input())
for __ in range(_):
    solve()
