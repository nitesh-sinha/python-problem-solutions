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

# Time complexity: O(N) where N is the number of nodes in the tree
# Space complexity: O(N) to store the nodes in the queue, which at max will be N/2 for a complete binary tree

from typing import Optional
from source.tree.definition.tree import TreeNode


class ReverseTraversal:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []
        if not root:
            return result

        # Use a queue for level-order traversal
        queue = [root]
        while queue:
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.pop(0)
                level_values.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the current level to the result
            result.append(level_values)
        
        # Reverse the result to get bottom-up order
        result.reverse()
        return result
