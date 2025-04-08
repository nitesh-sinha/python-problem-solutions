# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:

# Input: root = [4,2,7,1,3,6,9]

# # Generate a visual binary tree from the input
#              4
#            /   \
#           2     7
#          / \   / \
#         1   3 6   9


# Output: [4,7,2,9,6,3,1]

# # Generate a visual binary tree from the output
#              4
#            /   \
#           7     2
#          / \   / \
#         9   6 3   1

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h=height of the tree

from definition.tree import TreeNode
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            # null or single node tree
            return root
        
        tempNode: Optional[TreeNode] = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tempNode)
        return root 
        
