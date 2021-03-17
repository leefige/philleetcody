#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.57%)
# Likes:    11131
# Dislikes: 2660
# Total Accepted:    1.8M
# Total Submissions: 5.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# Example 2:
# 
# 
# Input: l1 = [0], l2 = [0]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # NOTE: though there is a trick that current = self, but the
        # stupid method head = ListNode(-1) actually saves space than
        # that smart way
        head = ListNode(-1)
        current = head
        carry = 0
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next
            l1, l2 = l1.next, l2.next
        
        # ensure l1 no shorter than l2
        if l2:
            l1, l2 = l2, l1

        while l1:
            sum_ = l1.val + carry
            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next
            l1 = l1.next

        if carry != 0:
            current.next = ListNode(carry)

        return head.next
# @lc code=end

