# Solution for 1009. Complement of Base 10 Integer
# Platform: LeetCode
# Date: 2026-03-11
#
def bitwiseComplement(n: int) -> int:
    if n == 0:
        return 1

    number_of_shifts = n.bit_length()
    i = 0
    while number_of_shifts > 0:
        n = n ^ (1 << i)
        number_of_shifts -= 1
        i += 1

    return n


if __name__ == "__main__":
    print(bitwiseComplement(int(input().strip())))
