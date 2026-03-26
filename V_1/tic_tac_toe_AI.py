import numpy as np
from copy import deepcopy


# Node class for keeping track of actions and state
class Node:
    def __init__(self, state, parent, action, cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.status = None


# a initial board with simple functionality
class Board:
    def __init__(self):
        self.board = np.array([[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]])

    # marks X or O in a given position
    def make_move(self, pos: tuple, mark: int):
        if mark not in [1, -1]:
            raise "Invalid input as marker"
        self.board[pos[0]][pos[1]] = mark
        return self.board


# algorithm to estimate a move to play
class CalculateMove_DSF:
    def __init__(self):
        self.total_steps = 0  # total number of nodes created
        self.end_branch_nodes = [] # collection terminating states


    # function that checks if game has ended ot not and assigns ebd game status to nodes
    @staticmethod
    def terminal( nodes):
        for mark in [3, -3]:
            if any(np.sum(nodes.state[i]) == mark for i in range(3)) or any(
                    np.sum(nodes.state[:, i]) == mark for i in range(3)) or np.sum(
                [nodes.state[i, i] for i in range(3)]) == mark or np.sum([nodes.state[2 - i, i] for i in range(3)]) == mark:
                nodes.status = 1 if mark == 3 else -1
                return True
            else:
                for i in range(3):
                    for j in range(3):
                        if nodes.state[i, j] == 0:
                            return False
                nodes.status = 0
                return True

    @staticmethod
    def remove_node(frontier):
        node = frontier[0]
        frontier = frontier[1:]
        return node, frontier

    @staticmethod
    def valid_moves(state):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if state[i, j] == 0:
                    valid_moves.append((i, j))
        return valid_moves

    @staticmethod
    def determine_player(state):
        total_moves = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == 1 or state[i][j] == -1:
                    total_moves += 1
        if total_moves % 2 == 0:
            return 1
        else:
            return -1

    def apply_action(self, state, action):
        move = self.determine_player(state)
        new_state = deepcopy(state)
        new_state[action[0], action[1]] = move
        return new_state

    def calculate(self, initial_state):
        initial_node = Node(state=deepcopy(initial_state), parent=None, action=None)
        frontier = [initial_node]
        while True:
            self.total_steps += 1
            print(self.total_steps)
            if not frontier:
                break
            node, frontier = self.remove_node(frontier)

            if self.terminal(node):
                self.end_branch_nodes.append(node)
                continue

            for action in self.valid_moves(node.state):
                state = self.apply_action(node.state, action)
                # print(state)
                acc_node = Node(state=state, action=action, parent=node, cost=node.cost + 1)
                frontier.append(acc_node)
            # print("___________________________________________________________________________________")


    @staticmethod
    def get_initial_state_node(end_node):
        node = deepcopy(end_node)
        while True:
            if node.parent.parent is None:
                return node
            node = node.parent

    def select_move(self, lower_limit : int):
        if not self.end_branch_nodes:
            print("No Solution")
            return None
        if lower_limit == -1:
            self.end_branch_nodes.sort(key=lambda x : (-x.status, x.cost))
            finial_node = self.get_initial_state_node(self.end_branch_nodes[0])
        else:
            self.end_branch_nodes.sort(key=lambda x : (x.status, x.cost))
            finial_node = self.get_initial_state_node(self.end_branch_nodes[-1])
            print("COst - >",finial_node.cost)
        return finial_node.action









