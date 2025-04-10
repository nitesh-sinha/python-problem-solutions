# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a 
# node to be a descendant of itself).”

# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# # visualize the tree
# #       6
# #      / \
# #     2   8
# #    / \ / \
# #   0  4 7  9
# #     / \
# #    3   5

# Example 2:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
# # visualize the tree
# #       2
# #      /
# #     1

# Time Complexity: O(N) where N is the number of nodes in the tree
# Space Complexity: O(N) for the recursive stack
# Best case: h=log(N) for a balanced tree
# Worst case: h=N for a skewed tree

from tree.definition.tree import TreeNode

class LCA:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            lca = root
        elif p.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            lca = self.lowestCommonAncestor(root.right, p, q)
        return lca
        

 