# Tic Tac Toe AI

This is my Tic Tac Toe AI project where I tried making the computer play the game by making decisions on its own instead of just using random moves.

Right now this project has 2 versions:

- `V_1` is my earlier attempt.
- `V_2` is the improved version and the better one to run.

## Why I made this

I wanted to understand how game decision making works in AI, so Tic Tac Toe felt like a good place to start. It is small enough to manage, but still good for learning search, board evaluation, recursion, and move selection.

## Project structure

### `V_1`

This version was my first serious attempt at solving the problem.

It explores board states and tries to pick a move from the generated results. It helped me understand:

- board representation
- valid move generation
- terminal state checking
- how search trees are built

But this version also had some clear issues:

- it was slow and inefficient
- the decision making was not very reliable
- it did not properly assume the opponent would always play the best move
- the final move selection logic still needed improvement

I already wrote some of these problems inside the code itself because this version was mainly for learning and testing ideas.

### `V_2`

This is the improved version of the project.

In this version I changed the logic to use the minimax algorithm, which made the AI much stronger and more consistent. Instead of just exploring states loosely, this version tries to calculate the best possible move while also assuming the opponent will respond properly.

Current things in `V_2`:

- playable in terminal
- computer plays as `X`
- user plays as `O`
- checks win, loss, and tie states
- prints the board in a cleaner format using `tabulate`

## Improvements from past version

Main improvements from `V_1` to `V_2`:

- changed from my earlier search approach to minimax
- better move selection
- cleaner gameplay loop
- better board display
- overall more practical and playable

So for me, `V_1` was more of a learning version, and `V_2` is the version where the project started feeling like an actual game.

## Future improvements

Things I may add in the next version:

- alpha-beta pruning to make minimax faster
- difficulty levels
- better user interface
- option to choose who plays first
- replay/restart option without rerunning the file
- cleaner input system with better prompts

## How to run

Run the improved version:

```bash
python V_2/main.py
```

If needed, install the required packages first:

```bash
py -m pip install -r requirements.txt
```

or 
```bash
python -m pip install -r requirements.txt
```

**Note : If this doesn't work, just google it**

## Final note

This project is mainly a learning project, but it also shows how my approach improved from one version to another. I wanted to keep the older version in the repo too because it shows the progress instead of only showing the final version.
