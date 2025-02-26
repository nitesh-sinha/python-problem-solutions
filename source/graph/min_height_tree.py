class MHT:
    def find_mht_roots(self, n: int, edges: list[list[int]]) -> list[int]:
        # Build adjacency list from edge list
        # Add all leaf nodes to a queue
        # Remove each leaf node from queue one by one and remove its connected edges and the leaf node itself.
        # Add new leaf nodes(to queue) formed as a result of edge/node deletion from previous step.
        # Continue this until 1 or 2 nodes remain(since a graph with no cycles can have at most 2 MHTs)
        if n == 1:
            return [0]
        adj_list: dict = {i: set() for i in range(n)}
        for edge_start, edge_end in edges:
            adj_list.get(edge_start).add(edge_end)
            adj_list.get(edge_end).add(edge_start)
        leaves = [node for node, neighbours in adj_list.items() if len(neighbours) == 1]
        while len(adj_list) > 2: # Atleast 2 nodes remain
            new_leaves = []
            for leaf in leaves:
                neighbour = adj_list.get(leaf).pop() # only 1 neighbour exists since its leaf node
                # remove edge from leaf to neighbour i.e.
                # remove leaf node as neighbour's connection from adj_list
                neighbour_edges = adj_list.get(neighbour)
                neighbour_edges.remove(leaf)
                if len(neighbour_edges) == 1:
                    new_leaves.append(neighbour)
                adj_list.update({neighbour: neighbour_edges})
                adj_list.pop(leaf)
            leaves = new_leaves
        return leaves


if __name__ == "__main__":
    mht = MHT()
    print(mht.find_mht_roots(4, [[1,0],[1,2],[1,3]]))
    print(mht.find_mht_roots(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    print(mht.find_mht_roots(1, []))


