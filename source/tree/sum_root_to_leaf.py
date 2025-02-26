# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.
#
# A leaf node is a node with no children.
#
# Example 1:
# #    1
# #   / \
# #  /   \
# #  2   5
# # / \   \
# # 3 4   6
# Output: 403
# Explanation: 123 + 124 + 156 = 403

from typing import Optional
from definition.tree import TreeNode


class PathsSum:
    def __init__(self):
        self.total_sum = 0
        self.path_nums = []

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        self.get_paths_sum(root)
        return self.total_sum

    def get_paths_sum(self, root) -> None:

        self.path_nums.append(root.val)
        if not root.left and not root.right:
            # leaf node
            # convert list of ints to list of str,
            # join to form str and then convert to int
            num = int("".join(map(str, self.path_nums)))
            self.total_sum += num
            self.path_nums = self.path_nums[:-1]  # remove last element
            return

        if root.left:
            self.get_paths_sum(root.left)
        if root.right:
            self.get_paths_sum(root.right)
        self.path_nums = self.path_nums[:-1]
