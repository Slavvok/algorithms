"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c: i for i, c in enumerate(s)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(s):

            right = max(right, rightmost[letter])

            if i == right:
                result += [right - left + 1]
                left = i + 1

        return result
