from functools import reduce

from timer import Timer
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""


class Solution1:
    @Timer(name="decorator")
    def reverse(self, x: int) -> int:
        """
        Dull and obvious solution
        :param x:
        :return:
        """
        border = 2**31 - 1
        x = str(x)
        minus = None
        if x[0] == "-":
            minus = x[0]
            x = x[1:]

        result = x[::-1]
        if int(result) > border:
            return 0
        if minus:
            result = minus + result
        return int(result)


class Solution2:
    @Timer(name="decorator")
    def reverse(self, x: int) -> int:
        """
        Recursion solution
        :param x:
        :return:
        """
        border = 2**31 - 1
        x = str(x)
        minus = None
        if x[0] == "-":
            minus = x[0]
            x = x[1:]

        result = self._reverse_str(x)
        if int(result) > border:
            return 0
        if minus:
            result = minus + result
        return int(result)

    def _reverse_str(self, x):
        if len(x) == 1:
            return x

        return self._reverse_str(x[1:]) + x[:1]


class Solution3:
    @Timer(name="decorator")
    def reverse(self, x: int) -> int:
        """
        Recursion solution
        :param x:
        :return:
        """
        border = 2**31 - 1
        x = str(x)
        minus = None
        if x[0] == "-":
            minus = x[0]
            x = x[1:]

        result = reduce(lambda a, b: b + a, x)
        if int(result) > border:
            return 0
        if minus:
            result = minus + result
        return int(result)


if __name__ == '__main__':
    num = -46257257

    result1 = Solution1().reverse(num)
    print(result1)
    result2 = Solution2().reverse(num)
    print(result2)
    result3 = Solution3().reverse(num)
    print(result3)
