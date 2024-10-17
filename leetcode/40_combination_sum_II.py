"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def combination(left, comb, target):
            if target < 0:
                return

            if target == 0:
                result.append(comb)
                return

            for i in range(left, len(candidates)):
                if i > left and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                combination(i + 1, comb + [candidates[i]], target - candidates[i], )

        combination(0, [], target)
        return result
