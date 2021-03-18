#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (31.47%)
# Likes:    13496
# Dislikes: 698
# Total Accepted:    2.1M
# Total Submissions: 6.6M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    """ O(2n)=O(n): start & end at most scan whole string once;
        use a sliding window to record chars btw [start, end).
        Worst case: abcdd (unique except for repeating last char).
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window, record chars in [start, end)
        window = {}
        leng = len(s)
        maxsub = 0

        # [start, end)
        start = 0
        end = start
        while start < leng:
            # try to extend end
            while end < leng:
                if s[end] not in window:
                    window[s[end]] = 1
                    end += 1
                else:
                    # valid: [start, end)
                    current_len = end - start
                    if current_len > maxsub:
                        maxsub = current_len
                    break

            # early stop, don't forget to check valid length again
            if end == leng:
                current_len = end - start
                if current_len > maxsub:
                    maxsub = current_len
                break

            # start chases end until find the repeating char
            while start < end and s[start] != s[end]:
                del window[s[start]]
                start += 1

            # now s[start] == s[end]
            start += 1
            end += 1

        return maxsub

# @lc code=end

# Accepted
# 987/987 cases passed (52 ms)
# Your runtime beats 92.84 % of python3 submissions
# Your memory usage beats 82.54 % of python3 submissions (14.3 MB)
