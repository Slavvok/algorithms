"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


class Solution:
    """
    Two loops solution
    72 ms, beats 83
    O(n + m)
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        s = set()

        for i in range(len(nums)):
            if nums[i] not in s:
                nums[len(s)] = nums[i]
                s.add(nums[i])

        for i in range(len(s), len(nums)):
            nums[i] = "_"

        return len(s)


if __name__ == '__main__':
    n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(n)
    assert result == 5
