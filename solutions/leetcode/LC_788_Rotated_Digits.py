# Solution for 788. Rotated Digits
# Platform: LeetCode
# Date: 2026-05-02
#
class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotation_hash = {
            0: 0,
            1: 1,
            2: 5,
            3: None,
            4: None,
            5: 2,
            6: 9,
            7: None,
            8: 8,
            9: 6,
        }

        NON_ROTATE = [3, 4, 7]

        def isGood(num):
            rotated = []
            for i in str(num):
                if int(i) in NON_ROTATE:
                    return False, None
                rotated.append(str(rotation_hash[int(i)]))
            return True, int("".join(rotated))

        res = 0
        for num in range(1, n + 1):
            _isGood, _num = isGood(num)
            if _isGood and _num != num:
                # print(_isGood, _num)
                res += 1

        return res
