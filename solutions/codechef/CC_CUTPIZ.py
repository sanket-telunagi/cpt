# Solution for Cutting Pizza
# Platform: codechef
# Date: 2026-01-19
#

import sys
import math


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    ptr = 1

    results = []
    for _ in range(T):
        if ptr >= len(input_data):
            break

        n = int(input_data[ptr])
        ptr += 1

        angles = []
        for _ in range(n):
            angles.append(int(input_data[ptr]))
            ptr += 1

        base_angle = angles[0]
        g = 360
        for i in range(1, n):
            diff = angles[i] - base_angle
            g = math.gcd(g, diff)

        total_slices_needed = 360 // g
        additional_cuts = total_slices_needed - n
        results.append(str(additional_cuts))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
