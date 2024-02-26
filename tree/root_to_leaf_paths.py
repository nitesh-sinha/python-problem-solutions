# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.

#Example:
#
#Input:
#
#           1
#         /   \
#        2     3
#         \
#          5
#
#Output: ["1->2->5", "1->3"]
#
#Explanation: All root - to - leaf paths are: 1->2->5, 1->3

from typing import Optional
from tree.definition.tree import TreeNode


class PathsGetter:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths = []
        if not root or (not root.left and not root.right):
            # 0 or 1 node tree
            paths.append(f"{root.val}")
            return paths

        self.get_paths(root, "", paths)
        return paths

    def get_paths(self, root, path, paths):
        if not root:
            return

        path += f"{root.val}"
        if not root.left and not root.right:
            # leaf node
            paths.append(path)
            return
        path += "->"
        self.get_paths(root.left, path, paths)
        self.get_paths(root.right, path, paths)