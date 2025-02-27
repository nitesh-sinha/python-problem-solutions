from definition.linkedlist import ListNode, LinkedList
from typing import Optional


class Rotator:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # Get length of list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        # Updates nodes connections
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_element(1)
    ll.add_element(2)
    ll.add_element(3)
    ll.add_element(4)
    LinkedList.print_linked_list(ll.head)
    r = Rotator()
    new_head = r.rotateRight(ll.head, 2)
    LinkedList.print_linked_list(new_head)
