# Fichier d'implémentation du IDS

# Importation des bibliothèques nécessaires
from .commun import is_goal_state, is_valid, PuzzleState, row, col

# Recherche en profondeur (DFS), retourne (état final ou None, nb d'états explorés, taille de la frontière à chaque itération)
def solve_puzzle_ids(start,x,y):
    iterations = 0
    frontier_sizes = []

    # spécifier la limite de profondeur
    limit = 0

    while True:
        stack = [PuzzleState(start, x, y, 0)]
        visited = {tuple(map(tuple, start)):0}

        # variable de sortie de boucle
        cutoff = False
        
        while stack:

            # taille de la frontière à chaque itération avant de pop()
            frontier_sizes.append(len(stack))

            curr = stack.pop()

            # état est exploré au moment du pop()
            iterations += 1

            # Vérifie si l'état final est atteint
            if is_goal_state(curr.board):
                return curr, iterations, frontier_sizes

            # arreter la boucle à chaque limite de profondeur atteinte
            if curr.depth == limit:
                cutoff = True
                continue

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

                    d = curr.depth + 1

                    if board_tuple not in visited or (visited[board_tuple] > d):
                        visited[board_tuple] = d
                        stack.append(PuzzleState(new_board, new_x, new_y, d, parent=curr))
        if not cutoff:
            return None, iterations, frontier_sizes
        limit+=1    
