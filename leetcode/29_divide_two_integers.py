"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -2**31 and b == -1:
            return 2**31 - 1

        sign = -1 if (a < 0) ^ (b < 0) else 1

        a, b = abs(a), abs(b)

        quotient = 0

        for i in range(31, -1, -1):
            if (b << i) <= a:
                a -= (b << i)
                quotient |= (1 << i)

        return sign * quotient
