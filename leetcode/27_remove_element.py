"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


class Solution:
    """
    Two pointers solution
    36 ms, beats 72 %
    O(n + m)
    """
    def removeElement(self, nums: list[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = "_"

        return j


if __name__ == '__main__':
    lst = [0, 1, 2, 2, 3, 0, 4, 2]
    value = 2
    result = Solution().removeElement(lst, value)

    assert result == 5
    assert lst == [0, 1, 3, 0, 4, "_", "_", "_"]
