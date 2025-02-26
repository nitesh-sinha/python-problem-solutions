from definition.tree import TreeNode
from btree_printer import BTreePrinter


class Inorder:
    def traverse(self, root: TreeNode) -> None:
        # Iterative inorder(Left -> root -> right)
        if not root:
            return

        stack = []
        cur_node = root
        while stack or cur_node:
            while cur_node:
                # keep inserting left child in stack
                stack.append(cur_node)
                cur_node = cur_node.left

            # no more left child,
            # keep track of cur right subtree in cur_node
            cur_node = stack.pop()
            print(cur_node.val)
            cur_node = cur_node.right


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
    print("======== In order traversal =========")
    i = Inorder()
    i.traverse(root)


# Solution #2: Recursive:
#
# if not root:
#     return
#
# self.traverse(root.left)
# print(root.val)
# self.traverse(root.right)