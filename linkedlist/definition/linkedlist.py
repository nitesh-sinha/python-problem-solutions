class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Needed to compare two ListNode objects, example when
    # adding them to a min heap. Check usage in
    # merge_k_sorted.py
    def __lt__(self, other):
        return self.val < other.val


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

    @classmethod
    def print_linked_list(cls, input_head=None):
        if not input_head:
            raise "Head is empty. Can't print anything!"
        ptr = input_head
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
    LinkedList.print_linked_list(ll.head)
