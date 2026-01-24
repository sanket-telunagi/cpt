# Solution for Final Verdict
# Platform: codeforces
# Date: 2026-01-19
#


# def solve():
#     t = int(input())
#     for _ in range(t):
#         n, x = map(int, input().split())

#         nums = list(map(int, input().split()))

#         avg = sum(nums) // n

#         print("YES" if avg == x else "NO")


# if __name__ == "__main__":
#     solve()


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
        x = int(input_data[pointer + 1])
        pointer += 2

        current_sum = 0
        for _ in range(n):
            current_sum += int(input_data[pointer])
            pointer += 1

        if current_sum == n * x:
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
