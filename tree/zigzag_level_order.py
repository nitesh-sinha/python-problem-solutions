#         Binary Tree Zigzag Level Order Traversal: Given a binary tree,
#         return the zigzag level order traversal of its nodes values.
#         (ie, from left to right, then right to left for the next level and alternate between).
# 
#         For example:
#         Given binary tree [3,9,20,null,null,15,7],
# 
#           3
#          / \
#         9  20
#        /  \
#       15   7
# 
#         return its zigzag level order traversal as:
# 
#         [
#         [3],
#         [20,9],
#         [15,7]
#         ]
#

from typing import Optional
from definition.tree import TreeNode
from collections import deque
from btree_printer import BTreePrinter

class ZigZagTraversal:
    def traverse(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        # Level order traversal of the binary tree using a queue
        res = []
        elem_queue = deque([root])
        level = 0
        while elem_queue:
            level_elements = [node.val for node in elem_queue]
            # check level and add elements in same or reverse order for zigzag effect
            res.append(level_elements if level % 2 == 0 else level_elements[::-1])
            # Flatten the next level of tree
            elem_queue = [child for node in elem_queue for child in (node.left, node.right) if child]
            level += 1

        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(9)
    root.right.left.right = TreeNode(-1)

    # Print the tree
    BTreePrinter.print_tree(root)
    traverser = ZigZagTraversal()
    print(traverser.traverse(root))

