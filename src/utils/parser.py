from typing import Literal

# mettre les litteraux de symboles vides possibles
BLANK_SYMBOLS = {"", "*", "_", "%", "\\"}

def parse_puzzle_file(filename: str) -> tuple[list[list[int | None]], int, int] | Literal[False]:
    lines_matrix = []
    blank_pos = None   # position de la case vide ou de référence à None

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 3:
                break
            # On nettoie le saut de ligne, puis on découpe strictement par tabulation
            row_str = line.replace("\n", "").replace("\r", "").split("\t")
            row_values = []

            # parcourt chaque valeur de la ligne pour la convertir en entier ou None si c'est un BLANK_SYMBOLS 
            for j, val in enumerate(row_str):
                val = val.strip()  # enlève superflus d'espace
                if val in BLANK_SYMBOLS:
                    row_values.append(None)
                    if blank_pos is None:
                        blank_pos = (i, j)  # On enregistre la position de la case vide
                elif val.isdigit():
                    row_values.append(int(val))
                else:
                    print(f"Valeur inattendue '{val}' dans le puzzle à la ligne {i + 1}, colonne {j + 1}")
                    return False     # pour signaler une erreur de format
            lines_matrix.append(row_values)

    if blank_pos is None:
        print("Erreur : aucune case vide trouvée dans le puzzle.")
        return False  # pour signaler une erreur de format encore

    return lines_matrix, blank_pos[0], blank_pos[1]