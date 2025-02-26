# Given the root of a binary tree, return the bottom-up level order traversal of its nodes values.
# (i.e., from left to right, level by level from leaf to root).
#
# Example 1:
#
#         -10
#         / \
#        /   \
#       9    20
#            / \
#          15   7
#
# Output: [[15,7], [9,20], [-10]]

from typing import Optional
from source.tree.definition.tree import TreeNode


class ReverseTraversal:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []
        if not root:
            return result

        levelq = [root]
        while levelq:
            level_values = []
            for i in range(len(levelq)):
                node = levelq.pop(0)
                level_values.append(node.val)
                if node.left:
                    levelq.append(node.left)
                if node.right:
                    levelq.append(node.right)

            result.insert(0, level_values)

        return result
