import os

import numpy as np
import math
from tabulate import tabulate
import keyboard
from copy import deepcopy


class Board:
    def __init__(self):
        self.board = np.array([None for _ in range(9)])
        self.board = self.board.reshape(3, 3)
        self.display_board = None

class Decision:
    def __init__(self, board, depth = 0, is_maximum = True):
        self.best_action = None
        self.player = "X" if is_maximum else "O"
        self.best_final_score = self.minimax(board, depth, is_maximum)


    @staticmethod
    def check_win(board, player):
        if any([all(board[i, j] == player for j in range(3)) for i in range(3)]) or any([all(board[j, i] == player for j in range(3)) for i in range(3)]) or all([board[i, i] == player for i in range(3)]) or all([board[i - 1, -i] == player for i in range(1, 4)]):
            return True
        else:
            return False

    @staticmethod
    def check_tie(board):
        if None not in board:
            return True
        else:
            return False

    @staticmethod
    def get_moves(board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i, j] is None:
                    moves.append((i, j))

        return moves
    def minimax(self, board, depth, is_maximum):
        if self.check_win(board,"X"):
            return 1
        if self.check_win(board, "O"):
            return -1
        if self.check_tie(board):
            return 0

        if is_maximum:
            best_score = -math.inf
            for move in self.get_moves(board):
                board[move] = "X"
                score = self.minimax(board, depth + 1, False)
                board[move] = None
                if depth == 0:
                    if score > best_score:
                        self.best_action = move
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.get_moves(board):
                board[move] = "O"
                score = self.minimax(board, depth + 1, True)
                board[move] = None
                if depth == 0:
                    if score > best_score:
                        self.best_action = move
                best_score = min(score, best_score)
            return best_score



game_board = Board()


while True:
    decision = Decision(game_board.board)
    game_board.board[decision.best_action] = "X"
    print(tabulate(game_board.board, tablefmt="fancy_grid"))
    print(f"Computer selected {decision.best_action} positon")

    if decision.check_win(game_board.board, "X"):
        print("Computer wins!")
        exit(0)
    if decision.check_tie(game_board.board):
        print("Game Ended in a tie!")
        exit(0)
    x = None
    y = None
    while True:
        try:
            x = int(input("Enter position x : "))
            y = int(input("Enter position y : "))
        except TypeError:
            print("Invalid input")
            continue

        if (x, y) not in decision.get_moves(game_board.board):
            print("Invalid Move Please enter correct position")
            continue

        game_board.board[(x, y)] = "O"
        break
    print(tabulate(game_board.board, tablefmt="fancy_grid"))
    print(f"You selected {(x, y)} position")
    if decision.check_win(game_board.board, "O"):
        print("You wins!")
        exit(0)
    if decision.check_tie(game_board.board):
        print("Game Ended in a tie!")
        exit(0)

