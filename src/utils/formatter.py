# Module qui écrit les résultats d'une exécution dans un fichier texte

import os

# écrit le fichier de sortie d'une exevution
def write_run_file( output_file, frontier_sizes, explored, elapsed_time):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        for i, size in enumerate(frontier_sizes, start=1):
            f.write(f"{i} \\t {size}\n")

        f.write(f"nombre_global_d_états_explorés: {explored}\n")
        f.write(f"temps d'exécution: {elapsed_time}\n")

# construit le chemin complet du fichier de sortie
def output_path(base_path, algo, input_file, run):
    name = os.path.splitext(os.path.basename(input_file))[0]
    return os.path.join(base_path,algo, f"{name}_run{run:02d}.txt")