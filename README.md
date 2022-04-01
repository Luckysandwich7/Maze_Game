Maze
====

Simple maze generator in Python. Can be used as a library to generate and
modify mazes, or run from the command line to play as a game.

When using as a game, the goal is to move `@`, using the arrow keys, to the
goal `$`.

Usage:
- `python maze.py` (uses default size of 20x10)
- `python maze.py 40 15` (specify size 40x15)
- `python maze.py 20` (square maze 20x20)

Contributors:
Ryan Alvord - 
Innocent Hove - 
Davi Vale - 

Example (don't worry, the lines look solid on the command line):

    python maze.py 18 12

    ┌───┬───────────────┬───────────────────┬───────────────────┬───────────┐
    │   │               │                   │                   │           │
    │   │   ┌───┐   ╷   │   ┌───┐   ╷   ┌───┘   ┌───────┐   ╷   └───╴   ╷   │
    │   │   │   │   │   │   │   │   │   │       │       │   │           │   │
    │   ╵   │   │   ├───┘   │   │   │   ╵   ┌───┘   ╷   ╵   ├───────┬───┘   │
    │       │   │   │       │   │   │       │       │       │       │       │
    │   ┌───┘   │   ╵   ┌───┤   └───┴───────┤   ┌───┴───────┤   ╷   ╵   ╶───┤
    │   │       │       │   │               │   │           │   │           │
    │   └───╴   └───┬───┘   ├───┬───────╴   │   │   ╶───┐   ├───┴───┬───┐   │
    │               │       │ @ │           │   │       │   │       │   │   │
    ├───────┬───┐   ╵   ╷   ╵   │   ┌───────┘   ├───╴   │   ╵   ╷   │   ╵   │
    │       │   │       │       │   │           │       │       │   │       │
    │   ╷   ╵   ├───────┘   ┌───┘   │   ╶───────┘   ┌───┴───────┤   └───────┤
    │   │       │           │       │               │           │           │
    │   └───┐   │   ┌───────┤   ╶───┴───────────────┤   ┌───╴   │   ╶───┐   │
    │       │   │   │       │                       │   │       │       │   │
    ├───╴   │   │   └───╴   └───────┬───┬───────╴   │   │   ╶───┴───┬───┘   │
    │       │   │                   │   │           │   │           │       │
    │   ┌───┘   ├───────┬───┬───╴   │   │   ╶───┬───┘   └───────┐   ╵   ╷   │
    │   │       │       │   │       │   │       │ $             │       │   │
    │   └───┐   ╵   ╷   ╵   │   ╶───┘   ├───┐   └───┐   ╶───┐   └───┬───┤   │
    │       │       │       │           │   │       │       │       │   │   │
    │   ╷   └───────┴───────┴───────╴   ╵   └───┐   └───────┴───╴   │   ╵   │
    │   │                                       │                   │       │
    └───┴───────────────────────────────────────┴───────────────────┴───────┘