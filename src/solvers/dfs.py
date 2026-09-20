# Fichier d'implémentation du DFS

# Importation des bibliothèques nécessaires

from .commun import is_goal_state, is_valid, PuzzleState, row, col

# Recherche en profondeur (DFS), retourne (état final ou None, nb d'états explorés, taille de la frontière à chaque itération)
def solve_puzzle_dfs(start: list[list[int | None]], x: int, y: int) -> tuple[PuzzleState | None, int, list[int]]:

    # LIFO
    stack = []
    visited = set()

    # Ajout de l'état de départ
    stack.append(PuzzleState(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    iterations = 0
    frontier_sizes = []

    while stack:
        # taille de la frontière à chaque itératiion avant de pop()
        frontier_sizes.append(len(stack))

        curr = stack.pop()

        # état est exploré au moment du pop()
        iterations += 1

        # Affiche le plateau courant
        # print(f'Profondeur: {curr.depth}')
        # print_board(curr.board)

        # Vérifie si l'état final est atteint
        if is_goal_state(curr.board):
            return curr, iterations, frontier_sizes

        # Explore les mouvements possibles
        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in curr.board]
                # Échange les cases
                new_board[curr.x][curr.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[curr.x][curr.y]

                # Si cet état n'a pas déjà été visité, l'empiler
                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1, parent=curr))

    return None, iterations, frontier_sizes
