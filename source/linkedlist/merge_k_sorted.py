# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
# Input: lists = []
# Output: []
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Time complexity: O(nk*log k) where n=average number of elements in each linkedlist, k=number of linkedlists
# Space complexity: O(k) for storing k elements in min heap

from definition.linkedlist import ListNode, LinkedList
from heapq import heappop, heappush, heapify


class MergeKSorted:
    def merge(self, lists: list[ListNode]) -> ListNode:
        min_heap = [lst for lst in lists if lst]
        heapify(min_heap)

        dummy = ListNode(0)
        tail: ListNode = dummy
        while min_heap: # this loop runs O(N) times where N is total number elements in all linked lists
            node = heappop(min_heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(min_heap, node.next) # This is O(log K) operation where K is no. of elements in heap

        return dummy.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.add_element(1)
    ll1.add_element(2)
    ll1.add_element(5)
    ll1.add_element(7)

    ll2 = LinkedList()
    ll2.add_element(2)
    ll2.add_element(3)
    ll2.add_element(6)
    ll2.add_element(8)

    ll3 = LinkedList()
    ll3.add_element(-1)
    ll3.add_element(0)

    merger = MergeKSorted()
    merged_head = merger.merge([ll1.head, ll2.head, ll3.head])
    #merged_head = merger.merge([])

    LinkedList.print_linked_list(merged_head)