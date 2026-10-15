# Solution for 3723. Maximize Sum of Squares of Digits
# Platform: LeetCode
# Date: 2026-10-14
#


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        def get_digits_sum(num):
            ct = 0
            digit_sum = 0
            digit_sq_sum = 0
            while num > 0:
                ct += 1
                digit_sum += num % 10
                digit_sq_sum += (num % 10) ** 2
                num //= 10
            return (ct, digit_sum, digit_sq_sum)

        left, right = 10 ** (num - 1), 10 ** (num)
        res = -1
        res_sq_sum = -1
        for n in range(right, left - 1, -1):
            # print(get_digits_sum(n), n, res_sq_sum)
            ct, digit_sum, digit_sq_sum = get_digits_sum(n)
            if ct == num and digit_sum == sum and digit_sq_sum > res_sq_sum:
                res = max(res, n)
                res_sq_sum = digit_sq_sum
                break

        return "" if res == -1 else str(res)
