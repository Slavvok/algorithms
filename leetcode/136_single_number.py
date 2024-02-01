"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            if d.get(i):
                del d[i]
            else:
                d[i] = 1
        return list(d.keys())[0]


class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor


if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]
    result = Solution().singleNumber(arr)
    print(result)

    arr = [4, 1, 2, 1, 2]
    result = Solution2().singleNumber(arr)
    print(result)
