"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        return self._binary_search(nums, l, r, target)

    def _binary_search(self, nums, low, high, target):
        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if nums[mid] == target:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif nums[mid] > target:
                return self._binary_search(nums, low, mid - 1, target)

            # Else the element can only be present in right subarray
            else:
                return self._binary_search(nums, mid + 1, high, target)

        else:
            # Element is not present in the array
            return -1


class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    result = Solution().search([-1, 0, 3, 5, 9, 12], 9)
    print(result)

    result = Solution2().search([-1, 0, 3, 5, 9, 12], 9)
    print(result)
