# Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which 
# the depth of the two subtrees of every node never differs by more than one.


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:

# Input: root = []
# Output: true


# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4

from definition.tree import TreeNode
from typing import Optional

class BalancedTreeChecker:
    # Algorithm 1: Top-down approach
    # Time complexity: O(N^2) since for each node, we check its left and right subtrees
    # Space complexity: O(h) where h=height of the tree, 
    # since max h frames are stored in the call stack at once at any point of time
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     return self.isBalanced(root.left) and self.isBalanced(root.right) \
    #         and abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1

    # def getHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     left_ht = 1 + self.getHeight(root.left)
    #     right_ht = 1 + self.getHeight(root.right)
    #     return max(left_ht, right_ht)

    
    # ALgorithm 2 : Bottom-up approach
    # Time complexity: O(N) since each node is processed exactly once
    # Space complexity: O(h) where h=height of the tree, 
    # since max h frames are stored in the call stack at once at any point of time
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalanced(root)[0]
    
    def checkBalanced(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        """Returns tuple of (is_balanced, height)"""
        if not root:
            return True, 0
            
        left_balanced, left_height = self.checkBalanced(root.left)
        if not left_balanced:
            return False, 0
            
        right_balanced, right_height = self.checkBalanced(root.right)
        if not right_balanced:
            return False, 0
            
        is_balanced = abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)
        
        return is_balanced, height
