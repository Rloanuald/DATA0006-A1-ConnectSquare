The game is similar to Connect Four, but the objective is to create a 2x2 square of four discs of the player's own color. Two tasks need to be completed: 

Task 1: Implement the "add coin" function that updates the game state after a move. It takes the current board, the player's coin, and the column where the coin is inserted. The function returns the new state of the board after the move.

Task 2: Create the "is winner" function to check if a player has won. It takes the current board and the player's coin as parameters and returns True if the player has won, False otherwise.

Task 3: Develop a heuristic for the AI player. The heuristic assigns values to different 2x2 squares on the board based on the presence of the player's coins and opponent's coins. The heuristic value for the game state is the sum of the values of all squares on the grid.

Task 4: Implement the AI player function, "ai move." It generates all possible moves, evaluates the resulting board states using the heuristic, and selects the move with the highest heuristic value. In case of a tie, the function chooses the move with the numerically lowest column. Finally, it returns the new board state after applying the best move.
