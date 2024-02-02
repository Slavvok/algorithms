"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        is_common = True
        curr_index = 0

        try:
            while is_common:
                prefix += strs[0][curr_index]
                for word in strs:
                    if word[:curr_index+1] != prefix:
                        is_common = False
                        prefix = prefix[:-1]
                        break
                curr_index += 1
        except IndexError:
            return prefix

        return prefix


class Solution1:
    def longestCommonPrefix(self, v: list[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans
