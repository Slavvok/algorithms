"""
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


class Solution:
    """
    Set solution
    854 ms, beats 24%
    """
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        seen = set()
        output = set()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    number = target - nums[i] - nums[j] - nums[k]
                    if number in seen:
                        res = sorted([nums[i], nums[j], nums[k], number])
                        output.add((res[0], res[1], res[2], res[3]))
            seen.add(nums[i])
        return list(list(i) for i in output)


if __name__ == '__main__':
    # l = [1, 3, 0, 4, 5, 2, -3]
    # result = Solution().fourSum(l, 9)

    l = [1, 0, -1, 0, -2, 2]
    result = Solution().fourSum(l, 0)
    print(result)
