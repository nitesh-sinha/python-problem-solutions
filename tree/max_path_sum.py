# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
# Example 1:
#  1
# / \
# 2 3
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
#
# Example 2:
#         -10
#         / \
#        /   \
#       9    20
#            / \
#          15   7
#
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


from typing import Optional
from definition.tree import TreeNode


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path_sum_helper(root):
            if not root:
                return 0
            # if left child is negative, eliminate it.
            # Hence we take max(left_gain, 0). Similarly for right
            # child
            left_gain = max(max_path_sum_helper(root.left), 0)
            right_gain = max(max_path_sum_helper(root.right), 0)

            # cur_path will always be (cur_root+left_gain+
            # right_gain) since that will always give max sum
            # if those 3 nodes are positive. Negative children case
            # is already accounted for, since we eliminted those negative
            # ones while calculating gains.
            cur_path_max = root.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, cur_path_max)
            # The max path to return will always include cur root
            # and the max of the left or right gain. We can't include
            # both gains here because the path will go via cur root
            # to the parent node of cur root. And so it can either the left
            # or right child of cur node(but not both).
            return root.val + max(left_gain, right_gain)

        max_path_sum_helper(root)
        return int(self.max_sum)
