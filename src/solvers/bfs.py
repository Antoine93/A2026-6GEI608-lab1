from collections import deque
from dataclasses import dataclass, field

N = 3

@dataclass(slots=True)
class PuzzleState:
    board: list[list[int]]
    x: int
    y: int
    depth: int = 0
    parent: 'PuzzleState | None' = None

row = (0, 0, -1, 1)
col = (-1, 1, 0, 0)

def is_goal_state(board: list[list[int]]) -> bool:
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal

def is_valid(x: int, y: int) -> bool:
    return 0 <= x < N and 0 <= y < N

def print_board(board: list[list[int]]) -> None:
    for r in board:
        print(' '.join(map(str, r)))
    print('--------')

def print_path(curr: PuzzleState | None) -> None:
    path = []
    while curr:
        path.append(curr)
        curr = curr.parent
    for state in reversed(path):
        print(f'Depth: {state.depth}')
        print_board(state.board)

def solve_puzzle_bfs(start: list[list[int]], x: int, y: int) -> tuple[PuzzleState | None, int]:
    q = deque([PuzzleState(start, x, y, 0)])
    q = deque([PuzzleState(start, x, y, 0)])
    visited = {tuple(map(tuple, start))}
    iterations = 0

    while q:
        curr = q.popleft()
        iterations += 1

        if is_goal_state(curr.board):
            #print(f'Goal state reached at depth {curr.depth}')
            #print(f'Total iterations (states popped): {iterations}\n')
            #print('Path to goal:')
            #print_path(curr)
            return curr, iterations

        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in curr.board]
                new_board[curr.x][curr.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[curr.x][curr.y]

                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    q.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1, parent=curr))

    return None, iterations