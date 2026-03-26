from tic_tac_toe_AI import *

board = Board()
board.board = np.array([[1, 0, -1],
                        [-1, 1, 0],
                        [0, 1, 0]])


brain = CalculateMove_DSF()
brain.calculate(board.board)
action = brain.select_move(-1)
print(brain.total_steps)

print(action)

board.make_move(action, 1)

print(board.board)


"""
Performance : Bad
Problem : 
1. doesn't think opponent with play the best
2. assume opponent as an dumb player or idiot i might say
3. no optimization
4. doesn't give the best move as result
5. no proper result validation or evaluation rules
6. need improvements in decision making
"""