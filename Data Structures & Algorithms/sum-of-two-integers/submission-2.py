
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            xorsum = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            a, b = xorsum, carry

        # if a is negative in 32-bit signed int
        return a if a <= MAX_INT else ~(a ^ MASK)