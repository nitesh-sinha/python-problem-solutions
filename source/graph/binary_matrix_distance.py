# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two cells sharing a common edge is 1.

# Example 1:

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]

# [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]

# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]

# [
#     [0, 0, 0],
#     [0, 1, 0],
#     [1, 1, 1]
# ]

# Output: [[0,0,0],[0,1,0],[1,2,1]]

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from collections import deque

class MinDistCalculator:
    # Algo:
        # Use a queue and enqueue all the cells with value 0 to start with.
        # Perform BFS:
            # From each 0, check its 4 neighbors (up, down, left, right).
            # If a neighbor has not yet been updated (i.e., current distance > new distance), 
                # update it and enqueue it.
        # Continue until the queue is empty.

    # Space complexity: O(m*n) where m=num rows of mat, n=num cols of mat
    # Time complexity: O(m*n)
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        bst_queue = deque()
        num_rows = len(mat)
        num_cols = len(mat[0])
        dist = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        dist_updated = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def canUpdateNewCell(new_cell_row: int, new_cell_col: int):
            return new_cell_row >= 0 and new_cell_row < num_rows \
                and new_cell_col >= 0 and new_cell_col < num_cols and \
                      not dist_updated[new_cell_row][new_cell_col]

        def updateNewCellDist(cur_row, cur_col, new_cell_row: int, new_cell_col: int):
            bst_queue.append((new_cell_row, new_cell_col))
            dist[new_cell_row][new_cell_col] = 1+dist[cur_row][cur_col]
            dist_updated[new_cell_row][new_cell_col] = True

        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    bst_queue.append((row, col))
                    dist_updated[row][col] = True
                
        while len(bst_queue) > 0:
            (cur_row, cur_col) = bst_queue.popleft()
            if canUpdateNewCell(cur_row-1, cur_col):
                updateNewCellDist(cur_row, cur_col, cur_row-1, cur_col)
            if canUpdateNewCell(cur_row+1, cur_col):
                updateNewCellDist(cur_row, cur_col, cur_row+1, cur_col)
            if canUpdateNewCell(cur_row, cur_col-1):
                updateNewCellDist(cur_row, cur_col, cur_row, cur_col-1)
            if canUpdateNewCell(cur_row, cur_col+1):
                updateNewCellDist(cur_row, cur_col, cur_row, cur_col+1)
            
        return dist
