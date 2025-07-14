"""
knight probability in chessboard
given a n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. each move, the knight chooses one of eight possible moves uniformly at random (even if the piece would go off the board) and moves there. the probability that the knight remains on the board after it has stopped moving is returned.
"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Initialize a 2D array to store the probability of the knight being at each cell after the current number of moves
        prev = [[0.0] * n for _ in range(n)]
        # The knight starts at (row, column) with probability 1
        prev[row][column] = 1.0

        # All possible moves a knight can make
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        # Repeat for each move from 1 to k
        for _ in range(k):
            # Initialize a new 2D array for the next move's probabilities
            curr = [[0.0] * n for _ in range(n)]
            # Loop through every cell on the board
            for i in range(n):
                for j in range(n):
                    # If the knight can be at (i, j) after the previous move
                    if prev[i][j] > 0:
                        # Try all possible knight moves from (i, j)
                        for dx, dy in directions:
                            ni, nj = i + dx, j + dy  # Calculate new position
                            # If the new position is on the board
                            if 0 <= ni < n and 0 <= nj < n:
                                # Add the probability of reaching (ni, nj) from (i, j)
                                curr[ni][nj] += prev[i][j] / 8.0
            # Update prev to be the current move's probabilities for the next iteration
            prev = curr

        # Sum the probabilities of the knight being on any cell after k moves
        return sum(prev[i][j] for i in range(n) for j in range(n))
