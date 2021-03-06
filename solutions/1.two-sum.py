#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (46.58%)
# Likes:    19816
# Dislikes: 697
# Total Accepted:    4M
# Total Submissions: 8.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#

# @lc code=start
class Solution:
    """ O(n) using hash table (dict/map) """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # remainder -> idx
        waiting = {}

        for i, num in enumerate(nums):
            if num in waiting:
                return [waiting[num], i]

            waiting[target - num] = i

        # should never come here
        assert False
        return [0, 1]

# @lc code=end

# Accepted
# 53/53 cases passed (48 ms)
# Your runtime beats 65.32 % of python3 submissions
# Your memory usage beats 46.77 % of python3 submissions (14.5 MB)
