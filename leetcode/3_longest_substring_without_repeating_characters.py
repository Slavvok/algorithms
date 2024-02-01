"""
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    @staticmethod
    def find_substring(s: str) -> int:
        d = dict()
        start = 0
        longest = 0

        for i in range(len(s)):
            curr = s[i]
            if d.get(curr, -1) >= start:
                start = d.get(curr) + 1
            longest = max(longest, i - start + 1)
            d[curr] = i
        return longest


if __name__ == '__main__':
    array1 = "abcabcbb"
    result1 = Solution().find_substring(array1)
    print(result1)

    array2 = "abcde"
    result2 = Solution().find_substring(array2)
    print(result2)
