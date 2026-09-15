# Fichier d'implémentation du DFS

# Importation des bibliothèques nécessaires
import time

from common import is_goal_state, is_valid, print_board
from collections import deque

# Mouvements possibles : Gauche, Droite, Haut, Bas
row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

# Structure pour stocker un état du puzzle
class PuzzleState:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

# Recherche en profondeur (DFS) pour résoudre le problème du taquin (8-puzzle)
def solve_puzzle_dfs(start, x, y):

    # démarrage du chronomètre de l'algorithme
    start_chrono = time.perf_counter()

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

            # arrêt du chronomètre de l'algorithme
            end_chrono = time.perf_counter()

            duration = end_chrono - start_chrono

            print(f"Temps d_exécution de la fonction de recherche : {duration} secondes")

            print(f'nombre_global_d_états_explorés {curr.depth}')

            return

        # Explore les mouvements possibles
        for i in range(4):
            new_x = curr.x + row[i]
            new_y = curr.y + col[i]

            if is_valid(new_x, new_y):
                new_board = [row[:] for row in curr.board]
                # Échange les cases
                new_board[curr.x][curr.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[curr.x][curr.y]

                # Si cet état n'a pas déjà été visité, l'empiler
                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(PuzzleState(new_board, new_x, new_y, curr.depth + 1))

    print('Aucune solution trouvée (DFS Brute Force, limite de profondeur atteinte)')

    
# Main Code
if __name__ == '__main__':
    start = [[1, 3, 6], [5, 4, 7], [2, '*', 8]]       # Start state
    x, y = 2, 1              # Position de '*' == "_"

    print('Start state:')
    print_board(start)

    solve_puzzle_dfs(start, x, y)
