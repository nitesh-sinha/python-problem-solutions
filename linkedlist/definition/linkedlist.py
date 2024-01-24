class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, num: int):
        ptr = self.head
        if not ptr:
            # adding first node
            self.head = ListNode(num)
            return

        while ptr.next:
            ptr = ptr.next
        # ptr is at end of linked list
        node = ListNode(num)
        ptr.next = node

    def print_linked_list(self, input_head = None):
        ptr = input_head if input_head else self.head
        while ptr:
            print(ptr.val, end="->")
            ptr = ptr.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_element(1)
    ll.add_element(2)
    ll.add_element(3)
    ll.add_element(4)
    ll.print_linked_list()
