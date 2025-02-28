class RandomNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.random = None

    # Sets random ptr of current node to dst_node
    def point_node_to(self, dst_node: "RandomNode"):
        self.random = dst_node
