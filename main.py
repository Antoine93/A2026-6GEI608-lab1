import time

from src.utils import parse_puzzle_file, write_run_file, output_path, is_solvable
from src.solvers import solve_puzzle_bfs, solve_puzzle_dfs,solve_puzzle_ids, print_board, print_path, get_actions

# ajout d'un dictionnaire pour mapper les algorithmes aux fonctions correspondantes
SOLVERS = {
    "bfs": solve_puzzle_bfs,
    "dfs": solve_puzzle_dfs,
    "ids": solve_puzzle_ids 
}

if __name__ == '__main__':
    #filename = "data/input-Ex1/Ex1-1.txt"
    filename = str(input("Nom du fichier (relatif) : "))
    parsed = parse_puzzle_file(filename)
    # Gestion des erreurs de parsing
    if parsed is False:
        print("Erreur lors de l'analyse du fichier. Veuillez vérifier le format.")
        exit(1)

    # demander à l'utilisateur quel algorithme utiliser
    algo = input("Algorithme à utiliser (bfs, dfs, ids) : ").strip().lower()
    if algo not in SOLVERS:
        print(f" '{algo}' non reconnu. Veuillez choisir parmi : {', '.join(SOLVERS.keys())}.")
        exit(1)

    solve = SOLVERS[algo]

    lines_matrix, x, y = parsed

    # condition pour vérifier si le puzzle est solvable avant de lancer la recherche
    ###### mettre cette section en commentaire pour voir qu'avec bfs et dfs, on a réussi à explorer tous les états ########
    if not is_solvable(lines_matrix):
        print("Le 8puzzle n'est pas solvable.")
        exit(1)

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
        result, iterations, frontier_sizes = solve(lines_matrix, x, y)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)

        path = output_path("results", algo, filename, run)
        write_run_file(path, frontier_sizes, iterations, end_time - start_time)

    average_time = total_time / N_RUNS
    print(f"Temps d'exécution moyen sur {N_RUNS} essais : {average_time:.6f} secondes")

    # Affichage des résultats après la série de mesures
    if result:
        actions = get_actions(result)

        print(f"Goal state atteint :")
        print_board(result.board)

        print(f'Distance : {len(actions)}')
        # print(f"Actions pour atteindre l'état objectif : {actions}")
        print(f"Nombre total d'itérations (états dépilés) : {iterations}\n")
    else:
        print(f"Aucune solution trouvée ({iterations} itérations vérifiées)")

