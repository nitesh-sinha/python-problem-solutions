from definition.tree import TreeNode

class BTreePrinter:
    @staticmethod
    def print_tree(root: TreeNode):
        _max_level = BTreePrinter._max_level(root)
        BTreePrinter._print_node_internal([root], 1, _max_level)

    @staticmethod
    def _print_node_internal(nodes, level, _max_level):
        if not nodes or BTreePrinter._is_all_elements_null(nodes):
            return

        floor = _max_level - level
        edge_lines = 2**(max(floor - 1, 0))
        first_spaces = 2**floor - 1
        between_spaces = 2**(floor + 1) - 1

        BTreePrinter._print_whitespaces(first_spaces)

        new_nodes = []
        for node in nodes:
            if node:
                print(node.val, end='')
                new_nodes.extend([node.left, node.right])
            else:
                new_nodes.extend([None, None])
                print(" ", end='')

            BTreePrinter._print_whitespaces(between_spaces)

        print()

        for i in range(1, edge_lines + 1):
            for j in range(len(nodes)):
                BTreePrinter._print_whitespaces(first_spaces - i)
                if not nodes[j]:
                    BTreePrinter._print_whitespaces(edge_lines + edge_lines + i + 1)
                    continue

                if nodes[j].left:
                    print("/", end='')
                else:
                    BTreePrinter._print_whitespaces(1)

                BTreePrinter._print_whitespaces(i + i - 1)

                if nodes[j].right:
                    print("\\", end='')
                else:
                    BTreePrinter._print_whitespaces(1)

                BTreePrinter._print_whitespaces(edge_lines + edge_lines - i)

            print()

        BTreePrinter._print_node_internal(new_nodes, level + 1, _max_level)

    @staticmethod
    def _print_whitespaces(count):
        for _ in range(count):
            print(" ", end='')

    @staticmethod
    def _max_level(node):
        if not node:
            return 0

        return max(BTreePrinter._max_level(node.left), BTreePrinter._max_level(node.right)) + 1

    @staticmethod
    def _is_all_elements_null(lst):
        return all(element is None for element in lst)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Print the tree
    BTreePrinter.print_node(root)