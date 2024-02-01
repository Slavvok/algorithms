"""
Given a string s, return the longest
palindromic

substring
 in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
from pprint import pprint


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = ""

        for i in range(1, len(s)):
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

            return max_str


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                print("Step", i, j)
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > Max_Len:
                        Max_Len = i - j + 1
                        Max_Str = s[j:i + 1]
                        print(i, j, Max_Str)
        pprint(dp)
        return Max_Str


if __name__ == '__main__':
    # s = "babad"
    s = "ebabxbag"
    result = Solution2().longestPalindrome(s)
    print(result)
