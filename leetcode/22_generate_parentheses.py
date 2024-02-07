"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

1 <= n <= 8
"""


class Solution:
    """
    Iterative solution
    48 ms
    Beats 18 %
    """
    def generateParenthesis(self, n: int) -> list[str]:

        output = []
        left, right = 0, 0
        stack = [(left, right, "")]

        while stack:
            left, right, curr = stack.pop()
            if len(curr) == 2 * n:
                output.append(curr)
            if left < n:
                stack.append((left + 1, right, curr + "("))
            if right < left:
                stack.append((left, right + 1, curr + ")"))

        return output


class Solution2:
    """
    Recursive solution
    44 ms
    Beats 31 %
    """

    def generateParenthesis(self, n: int) -> list[str]:

        def dfs(left, right, curr):

            if len(curr) == n * 2:
                output.append(curr)
                return

            if left < n:
                dfs(left + 1, right, curr + "(")
            if right < left:
                dfs(left, right + 1, curr + ")")

        output = []
        dfs(0, 0, "")
        return output


if __name__ == '__main__':
    result = Solution().generateParenthesis(3)
    assert result == ['()()()', '()(())', '(())()', '(()())', '((()))']

    result = Solution2().generateParenthesis(3)
    assert result == ['((()))', '(()())', '(())()', '()(())', '()()()']
