# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
# and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#
# Example 1:
#
#    1
#   / \
#  /   \
#  2   5
# / \   \
# 3 4   6
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
#
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [0]
# Output: [0]
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

from typing import Optional
from definition.tree import TreeNode
from btree_printer import BTreePrinter


class TreeFlattener:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            ptr = root.left
            while ptr.right:
                ptr = ptr.right
            ptr.right = root.right
            root.right = root.left
            root.left = None


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    root.left.left = TreeNode(3)
    BTreePrinter.print_tree(root)
    print("======== In order traversal =========")
    tf = TreeFlattener()
    tf.flatten(root)
