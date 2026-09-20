import time

from src.utils import parse_puzzle_file, write_run_file, output_path
from src.solvers import solve_puzzle_bfs, print_board, print_path

if __name__ == '__main__':
    #filename = "data/input-Ex1/Ex1-1.txt"
    filename = str(input("Nom du fichier (relatif) : "))
    
    parsed = parse_puzzle_file(filename)

    # Gestion des erreurs de parsing
    if parsed is False:
        print("Erreur lors de l'analyse du fichier. Veuillez vérifier le format.")
        exit(1)

    lines_matrix, x, y = parsed

    print('Initial State loaded from file:')
    print_board(lines_matrix)

    # Paramétrage du nombre de répétitions
    N_RUNS = 10
    total_time = 0.0
    result = None
    iterations = 0

    print(f"Exécution de la recherche {N_RUNS} fois pour calcul de la moyenne...")

    # Boucle de benchmarking
    for run in range(1, N_RUNS + 1):
        start_time = time.perf_counter()
        result, iterations, frontier_sizes = solve_puzzle_bfs(lines_matrix, x, y)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)

        path = output_path("results", "bfs", filename, run)
        write_run_file(path, frontier_sizes, iterations, end_time - start_time)

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