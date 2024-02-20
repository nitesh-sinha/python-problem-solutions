# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
# Example 2:
# Input: head = []
# Output: []
#
# Example 3:
# Input: head = [1]
# Output: [1]
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Time complexity: O(n) where n=number of nodes in linked list

from linkedlist.definition.linkedlist import ListNode
from typing import Optional


class SwapNodes:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head  # 0 or 1 node linked list

        prev, first, second = None, head, head.next
        head = second  # new head
        while first and second:
            first.next = second.next
            second.next = first
            if prev:
                prev.next = second
            # move all 3 pointers ahead
            prev = first
            first = first.next
            if first:
                second = first.next

        return head
