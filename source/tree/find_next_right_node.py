# Given a node of complete binary tree, return the right node of this node.

# The tree node has 3 pointers: left, right and parent.

#             A
#           /   \
#          B     C
#         / \   / \
#        D   E F   G 

#   - The depth of the tree is not known upfront.
  
#   Input    Output
#    A        null
#    B          C 
#    C        null
#    D          E 
#    E          F 
#    F          G 
#    G        null

from definition.parent_link_tree import ParentLinkTreeNode

class RightNodeFinder:
    # Iterative solution
    # Time complexity: O(h) where h=height of tree
    # Space complexity: O(1)
    def findNextRightNode(self, node: ParentLinkTreeNode) -> ParentLinkTreeNode:
        count = 0
        while node.parent and node.parent.right == node:
            # i am the right child of my parent
            node = node.parent
            count += 1

        # either we reached the root of tree or i am left child of my parent
        if not node.parent:
            # we reached root of tree
            return None
        
        # i am left child of my parent
        node = node.parent.right
        while count > 0:
            node = node.left
            count -= 1

        return node


    # Recursive solution:
    # Time complexity: O(h) where h=height of tree
    # Space complexity: O(h) for the recursive call stack
    # def findNextRightNode(self, node: ParentLinkTreeNode) -> ParentLinkTreeNode:
    #     # Base case
    #     if not node.parent:
    #         return None

    #     # if i am left child of my parent
    #     if node.parent.left == node:
    #         return node.parent.right

    #     # i am the right child of my parent
    #     parentsRightNode = self.findNextRightNode(node.parent)
    #     if not parentsRightNode:
    #         return None

    #     return parentsRightNode.left 
          

if __name__ == "__main__":
    nodeA = ParentLinkTreeNode("A")
    nodeB = ParentLinkTreeNode("B")
    nodeC = ParentLinkTreeNode("C")
    nodeD = ParentLinkTreeNode("D")
    nodeE = ParentLinkTreeNode("E")
    nodeF = ParentLinkTreeNode("F")
    nodeG = ParentLinkTreeNode("G")
    
    nodeA.left = nodeB
    nodeA.right = nodeC
    nodeB.parent = nodeA
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.parent = nodeA
    nodeC.left = nodeF
    nodeC.right = nodeG
    nodeD.parent = nodeB
    nodeE.parent = nodeB
    nodeF.parent = nodeC
    nodeG.parent = nodeC


    finder = RightNodeFinder()
    inputs = [nodeE, nodeF, nodeC, nodeA]
    for input in inputs:
        nextNode = finder.findNextRightNode(input)
        if nextNode != None:
            print(f"Node next to {input.val} is {nextNode.val}")
        else:
            print(f"Node next to {input.val} is Null")

