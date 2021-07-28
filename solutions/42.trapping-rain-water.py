#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.38%)
# Likes:    10725
# Dislikes: 159
# Total Accepted:    717.7K
# Total Submissions: 1.4M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    """
    O(n): 2 pointers to scan the height array
    From 2 ends to center, for left border you know the max height
    on its left, for right border you know the max height on its right
    (including left/right themselves).

    For left, its left_max_i = l_max; you also know its right_max_i >= r_max,
    so if l_max < r_max, then left_max_i < right_max_i, and trapped water at
    position left is decided by left_max_i == l_max. Just add l_max - height[left]
    to sum and increase left pointer by 1.
    """
    def trap(self, height: List[int]) -> int:
        size = len(height)

        if size <= 2:
            return 0

        # size >= 3
        trapped = 0
        l_max, r_max = -1, -1
        left, right = 0, size - 1
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                trapped += l_max - height[left]
                left += 1
            else:
                trapped += r_max - height[right]
                right -= 1

        return trapped



# @lc code=end

# Accepted
# 320/320 cases passed (44 ms)
# Your runtime beats 97.96 % of python3 submissions
# Your memory usage beats 37.41 % of python3 submissions (14.9 MB)
