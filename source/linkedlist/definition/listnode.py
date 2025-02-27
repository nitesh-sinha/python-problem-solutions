class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Needed to compare two ListNode objects, example when
    # adding them to a min heap. Check usage in
    # merge_k_sorted.py
    def __lt__(self, other: "ListNode") -> bool:
        return self.val < other.val