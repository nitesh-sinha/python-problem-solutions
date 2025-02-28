# You are given a singly linked list where each node has two pointers:
#
# next — Points to the next node.
# random — Points to any node in the list (or None).
#
# Write a function to create a deep copy of the list.
#
# Example:
#
# Input:
# Node1: 7 -> 13 -> 11 -> 10 -> 1
# Random pointers:
# Node1.random = None
# Node2.random = Node1
# Node3.random = Node5
# Node4.random = Node3
# Node5.random = Node1
#
# Output (Deep Copy):
# 7 -> 13 -> 11 -> 10 -> 1
# Random pointers:
# Node1.random = None
# Node2.random = Node1
# Node3.random = Node5
# Node4.random = Node3
# Node5.random = Node1
#
# Constraints:
# The number of nodes in the list is between 0 and 1000.
# Each node's value is between -10000 and 10000.

# Time Complexity: O(N) where N=no. of nodes in original linked list
# Space complexity: O(N)


from typing import Optional
from source.linkedlist.definition.randomlinkedlist import RandomLinkedList
from source.linkedlist.definition.randomnode import RandomNode


class DeepCopier:
    def copy_linked_list(self, original_list: RandomLinkedList) -> Optional[RandomNode]:
        original_to_copy_map: dict[RandomNode: RandomNode] = {}
        node = original_list.head
        # empty list
        if not node:
            return node

        # >=1 elements list(create the map of original to copied nodes w/o any pointers)
        while node:
            copied_node = RandomNode(node.val)
            original_to_copy_map[node] = copied_node
            node = node.next

        # add the pointers to copied list
        node = original_list.head
        head_copy = original_to_copy_map[original_list.head]
        while node:
            if node.next:
                original_to_copy_map[node].next = original_to_copy_map[node.next]
            if node.random:
                original_to_copy_map[node].random = original_to_copy_map[node.random]
            node = node.next

        return head_copy



if __name__ == "__main__":
    ll = RandomLinkedList()
    ll.add_element(7)
    ll.add_element(13)
    ll.head.next.random = ll.head  # 13.random -> 7

    deep_copier = DeepCopier()
    copied_head = deep_copier.copy_linked_list(ll)

    print(copied_head.val)  # 7
    print(copied_head.next.val)  # 13
    print(copied_head.next.random.val)  # 7
