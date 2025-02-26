# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


from source.tree.definition.tree import TreeNode
from typing import Optional

# Time complexity: O(n)
# Space complexity: O(1) + stack space for recursion
class BSTValidator:
    def __init__(self):
        self.prev_val = float('-inf')

    # traverse tree in-order and compare current node with
    # previously seen node. Return false as soon as invalid
    # case is encountered.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_validate_tree(root) -> bool:
            if not root:
                return True

            left_valid = traverse_validate_tree(root.left)
            if left_valid:
                # check current node's validity, iff
                # its left subtree is valid.
                cur_valid = root.val > self.prev_val
                self.prev_val = root.val
                if cur_valid:
                    # Only if left subtree and current node is valid,
                    # check validity of right subtree
                    right_valid = traverse_validate_tree(root.right)
            return left_valid and cur_valid and right_valid

        # 0 or 1 node tree
        if not root or (not root.left and not root.right):
            return True

        return traverse_validate_tree(root)
