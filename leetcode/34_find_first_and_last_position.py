"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, search_area):
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    ans = mid
                    if search_area == "right":
                        l = mid + 1
                    else:
                        r = mid - 1

            return ans

        left = binarySearch(nums, target, "left")
        right = binarySearch(nums, target, "right")

        return [left, right]
