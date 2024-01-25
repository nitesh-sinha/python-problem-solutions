# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
# and postorder is the postorder traversal of the same tree, construct and return the binary tree.
#
# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
# Constraints:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.


from typing import Optional
from definition.tree import TreeNode
from btree_printer import BTreePrinter


class TreeBuilder:
    def build(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # Read from postorder from the end will give us nodes
        # in the order root, right, left
        # Get root of tree by reading from postorder
        if inorder:
            root_val = postorder.pop()
            #print(root_val)
            inorder_index = inorder.index(root_val)

            # create root node
            root = TreeNode(root_val)

            # construct tree from right to left manner since we're reading
            # in thst order from postorder list
            root.right = self.build(inorder[inorder_index+1:], postorder)
            root.left = self.build(inorder[:inorder_index], postorder)

            return root

        return None

if __name__ == "__main__":
    builder = TreeBuilder()
    root = builder.build([9,3,15,20,7], [9,15,7,20,3])
    #root = builder.build([9,15,20,3,8,4,7], [15,20,9,8,4,7,3])
    #root = builder.build([3,2,1], [3,2,1])
    #root = builder.build([-1], [-1])
    #root = builder.build([], [])
    BTreePrinter.print_tree(root)