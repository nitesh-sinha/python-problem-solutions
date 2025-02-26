from definition.tree import TreeNode
from btree_printer import BTreePrinter


class Inorder:
    def traverse(self, root: TreeNode, lst: list) -> None:
        print(f"list = {lst}")
        if not root:
            return

        self.traverse(root.left, lst)
        print(root.val)
        lst.append(root.val)
        self.traverse(root.right, lst)
        #lst = lst[:-1] # this creates a new local variable lst which doesn't have last element of input lst arg. It doesn't modify the original lst arg list.
        lst.pop() # This will modify the original lst arg in-place.


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    #root.left.right.right = TreeNode(9)
    #root.right.left.right = TreeNode(-1)

    # Print the tree
    BTreePrinter.print_tree(root)
    print("======== In order traversal =========")
    i = Inorder()
    lst = []
    i.traverse(root, lst)
    print(f"In main lst={lst}")


# Solution #2: Recursive:
#
