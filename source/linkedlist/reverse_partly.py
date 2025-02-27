# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#

from typing import Optional
from definition.linkedlist import LinkedList, ListNode


class Reverse:
    def reverse_between(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Get pointers to left and right nodes
        left_ptr_prev = None
        left_ptr = head
        for i in range(left - 1):
            left_ptr_prev = left_ptr
            left_ptr = left_ptr.next

        right_ptr = left_ptr
        right_ptr_next = right_ptr.next
        for i in range(right - left):
            right_ptr = right_ptr.next
            right_ptr_next = right_ptr.next

        # Another pass over linkedlist from head
        # to reverse the relevant nodes
        before, cur = right_ptr_next, left_ptr
        while cur != right_ptr_next:
            after = cur.next
            cur.next = before
            before = cur
            cur = after

        if left_ptr_prev:
            # Set the link from part before linked list
            # to part after reversed list
            left_ptr_prev.next = right_ptr
        if left == 1:
            # this node would not be
            # the new head after reversal
            head = right_ptr
        return head


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_element(1)
    ll.add_element(2)
    ll.add_element(3)
    ll.add_element(4)
    LinkedList.print_linked_list(ll.head)
    rev = Reverse()
    new_head = rev.reverse_between(ll.head, 1,3)
    LinkedList.print_linked_list(new_head)

