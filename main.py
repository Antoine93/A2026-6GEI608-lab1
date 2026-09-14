import time

from utils import parse_puzzle_file
from solvers import solve_puzzle_bfs, print_board, print_path

if __name__ == '__main__':
    #filename = "data/input-Ex1/Ex1-1.txt"
    filename = str(input("Nom du fichier (relatif) : "))
    
    lines_matrix, x, y = parse_puzzle_file(filename)

    print('Initial State loaded from file:')
    print_board(lines_matrix)

    # Paramétrage du nombre de répétitions
    N_RUNS = 10
    total_time = 0.0
    result = None
    iterations = 0

    print(f"Exécution de la recherche {N_RUNS} fois pour calcul de la moyenne...")

    # Boucle de benchmarking
    for _ in range(N_RUNS):
        start_time = time.perf_counter()
        result, iterations = solve_puzzle_bfs(lines_matrix, x, y)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)

    average_time = total_time / N_RUNS

    # Affichage des résultats après la série de mesures
    if result:
        print('Chemin vers la solution :')
        print_path(result)
        print(f'État objectif atteint à la distance {result.depth}')
        print(f"Total d'itérations (états dépilés) : {iterations}\n")
    else:
        print(f"Aucune solution trouvée ({iterations} itérations vérifiées)")

    print(f"Temps d'exécution moyen sur {N_RUNS} essais : {average_time:.6f} secondes")