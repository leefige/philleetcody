#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (31.19%)
# Likes:    9508
# Dislikes: 1462
# Total Accepted:    889.7K
# Total Submissions: 2.8M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#

from typing import List

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # len(nums1) <= len(nums2)
        len1, len2 = len(nums1), len(nums2)
        assert len1 <= len2

        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[len2 // 2 - 1] + nums2[len2 // 2]) / 2
            else:
                return nums2[len2 // 2]

        total_len = len1 + len2
        # ceil(half len)
        half_len = (len1 + len2 + 1) // 2

        # nums1 : [0, i-1], [i, len1-1]
        # nums2 : [0, j-1], [j, len2-1]
        left_i = 0
        right_i = len1
        while left_i <= right_i:
            i = (left_i + right_i) // 2
            j = half_len - i

            if i < len1 and nums2[j-1] > nums1[i]:
                # NOTE: +1
                left_i = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # NOTE: -1
                right_i = i - 1
            else:
                break

        # i, j must exist
        if i == 0:
            left_max = nums2[j-1]
        elif j == 0:
            left_max = nums1[i-1]
        else:
            left_max = max(nums1[i-1], nums2[j-1])

        if i == len1:
            right_min = nums2[j]
        elif j == len2:
            right_min = nums1[i]
        else:
            right_min = min(nums1[i], nums2[j])

        if total_len % 2 == 1:
            return left_max
        else:
            return (left_max + right_min) / 2


# @lc code=end

s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([], [1]))

# Accepted
# 2094/2094 cases passed (84 ms)
# Your runtime beats 94.52 % of python3 submissions
# Your memory usage beats 27.7 % of python3 submissions (14.7 MB)
