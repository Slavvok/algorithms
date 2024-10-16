"""

"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combination(idx, comb, total):
            if total == target:
                result.append(comb[:])
                return

            if total > target or idx >= len(candidates):
                return

            comb.append(candidates[idx])
            combination(idx, comb, total + candidates[idx])
            comb.pop()
            combination(idx + 1, comb, total)
            return result

        return combination(0, [], 0)
