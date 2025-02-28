from source.linkedlist.definition.randomnode import RandomNode

class RandomLinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, num: int):
        ptr = self.head
        if not ptr:
            # adding first node
            self.head = RandomNode(num)
            return

        while ptr.next:
            ptr = ptr.next
        # ptr is at end of linked list
        ptr.next = RandomNode(num)

