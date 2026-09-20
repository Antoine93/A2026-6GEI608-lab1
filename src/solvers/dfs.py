# Fichier d'implémentation du DFS

# Importation des bibliothèques nécessaires
from .commun import is_goal_state, is_valid, PuzzleState, row, col

# Recherche en profondeur (DFS) pour résoudre le problème du taquin (8-puzzle)
def solve_puzzle_dfs(start, x, y):

    # LIFO
    stack = []
    visited = set()

    # Ajout de l'état de départ
    stack.append(PuzzleState(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while stack:
        curr = stack.pop()

        # Affiche le plateau courant
        # print(f'Profondeur: {curr.depth}')
        # print_board(curr.board)

        # Vérifie si l'état final est atteint
        if is_goal_state(curr.board):
            return

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

    print('Aucune solution trouvée (DFS Brute Force, limite de profondeur atteinte)')
