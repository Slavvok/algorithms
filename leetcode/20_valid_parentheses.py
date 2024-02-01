"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        curr_state = []
        for i in s:
            if d.get(i):
                if d[i] == curr_state[-1]:
                    curr_state.pop()
                else:
                    return False

            if i in d.values():
                curr_state.append(i)

        if curr_state:
            return False
        return True


if __name__ == '__main__':
    arr = "()[]{}"
    result = Solution().isValid(arr)
    print(result)

    arr2 = "([]{})"
    result2 = Solution().isValid(arr)
    print(result)
