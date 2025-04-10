# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

# Input: root = [2,1,3]
# Output: true

# # Visualize the tree
# #       2
# #      / \
# #     1   3


# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# # # Visualize the tree
# # #       5
# # #      / \
# # #     1   4
# # #        / \
# # #       3   6

# Explanation: The root node's value is 5 but its right child's value is 4.


# Example 3:

# Input: root = [5,1,6,null,null,3,8]
# Output: false
# # Visualize the tree
# #       5
# #      / \
# #     1   6
# #        / \
# #       3   8

## Time complexity: O(N) where N is the number of nodes in the tree
## Space complexity: O(N) for the recursive stack

from tree.definition.tree import TreeNode
from typing import Optional

class BSTValidator:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root: Optional[TreeNode], min_val, max_val) -> bool:
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False
        
        return self.isValidBSTHelper(root.left, min_val, root.val) and \
            self.isValidBSTHelper(root.right, root.val, max_val)
        



