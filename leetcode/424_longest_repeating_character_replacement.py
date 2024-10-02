"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)  # length of the string
        maxl = 0  # max frequency of a character in the current window
        ans = 0   # stores the longest valid window length
        l = 0     # left pointer
        count = {}  # dictionary to store character frequencies

        # Right pointer 'r' iterates over the string
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1  # Increase frequency of s[r]
            maxl = max(maxl, count[s[r]])  # Update max frequency in the current window

            # Check if the window is invalid (i.e., more than 'k' replacements needed)
            if (r - l + 1) - maxl > k:
                count[s[l]] -= 1  # Reduce frequency of the character at the left pointer
                l += 1  # Shrink the window by moving the left pointer forward

            # Update the answer with the maximum valid window size
            ans = max(ans, r - l + 1)

        return ans
