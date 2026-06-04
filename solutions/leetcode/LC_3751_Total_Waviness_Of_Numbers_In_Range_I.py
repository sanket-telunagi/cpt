# Solution for 3751. Total Waviness of Numbers in Range I
# Platform: LeetCode
# Date: 2026-06-04
#


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        n1, n2 = num1, num2
        res = 0
        if n2 < 100:
            return 0
        for i in range(n1, n2 + 1):
            n = i
            digits = []
            if n > 100:
                while n > 0:
                    digits.append(n % 10)
                    n //= 10
                digits = list(reversed(digits))

                for d in range(1, len(digits) - 1):
                    _prev = digits[d - 1]
                    _curr = digits[d]
                    _next = digits[d + 1]

                    if _prev < _curr > _next:
                        res += 1
                    elif _prev > _curr < _next:
                        res += 1

        return res
