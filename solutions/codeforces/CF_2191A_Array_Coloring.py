# Solution for CF_2191A_Array_Coloring
# Platform: codeforces
# Date: 2026-01-17
#

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    pointer = 1

    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        pointer += 1

        arr = []
        for i in range(n):
            arr.append((int(input_data[pointer]), i))
            pointer += 1

        arr.sort()

        possible = True
        for i in range(n - 1):
            parity1 = arr[i][1] % 2
            parity2 = arr[i + 1][1] % 2

            if parity1 == parity2:
                possible = False
                break

        if possible:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))


if __name__ == "__main__":
    solve()
