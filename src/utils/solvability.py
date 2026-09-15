# peut ne pas etre utile
# vériifie si le plateau est résolvable en comptant le nombre d'inversions
# résolvable si inversion pair car on a une grille de 3x3, à l'exception de la case vide () qui ne compte pas

def is_solvable(board: list[list[int | None]]) -> bool:

    # aplatir le tableau en une seule liste et ignorer la case vide (None)
    sequence = [num for row in board for num in row if num is not None]
    inversions = 0

    # contient nombre de tuiles à compter pour les inversions
    n = len(sequence)

    for i in range(n):
        for j in range(i + 1, n):
            # grande valeur placée avant valeur petite = 1 inversion
            if sequence[i] > sequence[j]:
                inversions += 1
    return inversions % 2 == 0
