# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

from typing import Optional
from definition.tree import TreeNode
from btree_printer import BTreePrinter

class TreeBuilder:
    def build(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Get root of tree by reading from preorder
        if inorder:
            root_val = preorder.pop(0)
            #print(root_val)
            inorder_index = inorder.index(root_val)

            # create root node
            root = TreeNode(root_val)

            # inorder list ensures that left of root is the left subtree
            # and right of root is the right subtree
            root.left = self.build(preorder, inorder[:inorder_index])
            root.right = self.build(preorder, inorder[inorder_index+1:])

            return root

        return None

if __name__ == "__main__":
    builder = TreeBuilder()
    #root = builder.build([3,9,20,15,7], [9,3,15,20,7])
    root = builder.build([3,9,20,15,7,4,8], [9,15, 20,3,8,4,7])
    #root = builder.build([-1], [-1])
    #root = builder.build([], [])
    BTreePrinter.print_tree(root)