/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (31.03%)
 * Likes:    12293
 * Dislikes: 751
 * Total Accepted:    1.4M
 * Total Submissions: 4.5M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, return the longest palindromic substring in s.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "cbbd"
 * Output: "bb"
 *
 *
 * Example 3:
 *
 *
 * Input: s = "a"
 * Output: "a"
 *
 *
 * Example 4:
 *
 *
 * Input: s = "ac"
 * Output: "a"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 1000
 * s consist of only digits and English letters (lower-case and/or
 * upper-case),
 *
 *
 */

#include <string>

using namespace std;

// @lc code=start
/**
 * @brief O(n^2): 2(n-1) centers, each expands at most n / 2; possible to early-stop (not impl).
 * Totally 2*(n-1) centers, including "gap" btw two chars.
 * Note: std::string::substring(Start, Count), instead of [left, right).
 */
class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.length();
        if (len <= 0) {
            return "";
        }

        int start = 0;
        int count = 1;

        for (int i = 0; i < 2 * (len - 1); i++) {
            int left, right;

            // center at char
            if (i % 2 == 0) {
                left = i / 2 - 1;
                right = i / 2 + 1;
            } else {
                left = i / 2;
                right = i / 2 + 1;
            }

            while (left >= 0 && right < len && s[left] == s[right]) {
                left--;
                right++;
            }
            // first time failure
            if (right - left - 1 > count) {
                start = left + 1;
                count = right - left - 1;
            }
        }

        return s.substr(start, count);
    }
};
// @lc code=end

// Accepted
// 177/177 cases passed (12 ms)
// Your runtime beats 94.97 % of cpp submissions
// Your memory usage beats 92.4 % of cpp submissions (7.1 MB)