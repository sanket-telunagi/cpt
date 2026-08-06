# Solution for 3345. Smallest Divisible Digit Product I
# Platform: LeetCode
# Date: 2026-08-06
#
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod_digits(num) :
            p = 1
            while num > 0 :
                p *= num%10
                num //= 10
            return p
        mx = 10_00_00_00
        for num in range(n, mx) :
            if prod_digits(num) % t == 0 :
                return num

        return -1
