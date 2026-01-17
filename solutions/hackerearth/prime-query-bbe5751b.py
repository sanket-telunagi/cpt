# Solution for prime-query-bbe5751b
# Platform: hackerearth
# Date: 2026-01-17
#
# for _ in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     q = int(input())
#     queries = []
#     for __ in range(q):
#         queries.append(tuple(map(int, input().split())))

#     # def isPrime(val):
#     #     for num in range(2, round(val**0.5)):
#     #         if val % num:
#     #             return False
#     #     return True

#     for L, R in queries:
#         count = 0
#         temp = nums[L - 1 : R + 1]
#         for i in range(len(temp) - 1):
#             for j in range(i + 1, len(temp)):
#                 val = temp[i] + temp[j]
#                 # print(temp[i], temp[j], val)
#                 # if isPrime(val):
#                 #     count += 1
#                 if val not in [0, 1]:
#                     count += 1

#         print(count)


# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     zero = [0] * n
#     one = [0] * n

#     for i in range(n):
#         if a[i] == 0:
#             zero[i] = 1
#             if a[i] == 1:
#                 one[i] = 1
#                 if i > 0:
#                     zero[i] += zero[i - 1]
#                     one[i] += one[i - 1]

#     q = int(input())
#     for _ in range(q):
#         l, r = map(int, input().split())
#         l -= 1
#         r -= 1

#         x = zero[r]
#         if l > 0:
#             x -= zero[l - 1]

#         y = one[r]
#         if l > 0:
#             y -= one[l - 1]

#         len = r - l + 1
#         c = (len * (len - 1)) // 2
#         c -= (x * (x - 1)) // 2
#         c -= x * y

#         print(c - 1)


# def main():
#     T = int(input())
#     for _ in range(T):
#         solve()


# if __name__ == "__main__":
#     main()


import sys


def solve():
    # Read all input at once for faster processing
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)

    # Get number of test cases
    try:
        t_str = next(it)
    except StopIteration:
        return
    t = int(t_str)

    output = []

    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        # Prefix sum arrays for 0s and 1s
        zero = [0] * n
        one = [0] * n

        for i in range(n):
            # Calculate current counts
            z_curr = 1 if a[i] == 0 else 0
            o_curr = 1 if a[i] == 1 else 0

            if i == 0:
                zero[i] = z_curr
                one[i] = o_curr
            else:
                zero[i] = zero[i - 1] + z_curr
                one[i] = one[i - 1] + o_curr

        q = int(next(it))
        for _ in range(q):
            l = int(next(it)) - 1
            r = int(next(it)) - 1

            # Range sum for zeros
            x = zero[r]
            if l > 0:
                x -= zero[l - 1]

            # Range sum for ones
            y = one[r]
            if l > 0:
                y -= one[l - 1]

            length = r - l + 1

            # Combinatorics logic matching the C++ code
            # total combinations = len * (len - 1) / 2
            total_combinations = (length * (length - 1)) // 2
            # zero_pairs = x * (x - 1) / 2
            zero_pairs = (x * (x - 1)) // 2
            # zero_one_pairs = x * y
            zero_one_pairs = x * y

            ans = total_combinations - zero_pairs - zero_one_pairs
            output.append(str(ans))

    # Print all answers joined by newline for efficiency
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
