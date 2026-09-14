def parse_puzzle_file(filename: str) -> tuple[list[list[int]], int, int]:
    lines_matrix = []
    zero_pos = (-1, -1)

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= 3:
                break
            # On nettoie le saut de ligne, puis on découpe strictement par tabulation
            row_str = line.replace("\n", "").split("\t")
            row_ints = [int(val) if val.isdigit() else 0 for val in row_str]
            lines_matrix.append(row_ints)
            
            # Recherche de la case vide (0) à la volée
            if 0 in row_ints:
                zero_pos = (i, row_ints.index(0))

    return lines_matrix, zero_pos[0], zero_pos[1]