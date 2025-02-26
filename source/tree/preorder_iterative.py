from definition.tree import TreeNode
from btree_printer import BTreePrinter

class Preorder:
    def iterative_traverse(self, root) -> None:
        if not root:
            return
        stack: list = [root]

        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    #root.left.right.right = TreeNode(9)
    #root.right.left.right = TreeNode(-1)

    # Print the tree
    BTreePrinter.print_tree(root)
    print("======== Pre order traversal =========")
    p = Preorder()
    p.iterative_traverse(root)