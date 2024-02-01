"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


class Solution:
    @staticmethod
    def median(arr1, arr2):
        output = Solution()._quicksort(arr1 + arr2)

        middle = len(output) // 2
        remain = len(output) % 2
        if remain == 1:
            result = output[middle]
        else:
            result = (output[middle] + output[middle-1]) / 2
        return result

    def _quicksort(self, arr):
        print(arr)
        if len(arr) < 2:
            return arr

        pivot = arr[0]

        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i >= pivot]

        return self._quicksort(less) + [pivot] + self._quicksort(greater)


class Solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = sorted(nums1)
        B = sorted(nums2)
        n = len(A)
        m = len(B)

        if (n > m):
            return self.findMedianSortedArrays(B, A)

        start = 0
        end = n

        median = (n + m + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = median - mid

            leftA = A[leftAsize - 1] if (leftAsize > 0) else float("-inf")
            leftB = B[leftBsize - 1] if (leftBsize > 0) else float("-inf")
            rightA = A[leftAsize] if (leftAsize < n) else float("inf")
            rightB = B[leftBsize] if (leftBsize < m) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)
            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1


if __name__ == '__main__':
    a1 = [1, 30, 50]
    a2 = [2, 40, 60]
    result = Solution().median(a1, a2)
    print(result)
