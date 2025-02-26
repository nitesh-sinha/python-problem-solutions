from typing import Optional
from source.tree.definition.tree import TreeNode
from source.tree.btree_printer import BTreePrinter


class BSTCreator:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == "__main__":
    bst = BSTCreator()
    bst_root = bst.sortedArrayToBST([-10,-3,0,5,9])
    BTreePrinter.print_tree(bst_root)


    ## Another algo:
    # def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
    #     return self.create_balanced_tree(nums, 0, len(nums) - 1)
    #
    # def create_balanced_tree(self, nums, start, end) -> Optional[TreeNode]:
    #     if end < start:
    #         return None
    #
    #     mid = start + (end - start) // 2
    #     root = TreeNode(nums[mid])
    #     root.left = self.create_balanced_tree(nums, start, mid - 1)
    #     root.right = self.create_balanced_tree(nums, mid + 1, end)
    #     return root