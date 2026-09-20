from collections import deque

# import des fonctions communes nécessaires à BFS
from .commun import PuzzleState, is_goal_state, is_valid, print_board, print_path, row, col

def solve_puzzle_bfs(start: list[list[int | None]], x: int, y: int) -> tuple[PuzzleState | None, int]:
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