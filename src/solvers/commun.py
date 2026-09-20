# fichier qui contient les fonctions communes aux différents algos
from dataclasses import dataclass

# actions selon le déplacement (x,y) de notre référence (case vide ou autre) 
ACTION= {
    (0, -1): "Gauche",
    (0, 1): "Droite",
    (-1, 0): "Haut",
    (1, 0): "Bas"
}

N = 3

# Structure pour stocker un état du puzzle
@dataclass(slots=True)
class PuzzleState:
    board: list[list[int | None]]
    x: int
    y: int
    depth: int = 0
    parent: 'PuzzleState | None' = None

# Mouvements possibles : Gauche, Droite, Haut, Bas
row = (0, 0, -1, 1)
col = (-1, 1, 0, 0)

def is_goal_state(board: list[list[int | None]]) -> bool:
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
    return board == goal

def is_valid(x: int, y: int) -> bool:
    return 0 <= x < N and 0 <= y < N

def print_board(board: list[list[int | None]]) -> None:
    for r in board:
        print(' '.join(map(str, r)))
    print('--------')

def print_path(curr: PuzzleState | None) -> None:
    path = []
    while curr:
        path.append(curr)
        curr = curr.parent
    for state in reversed(path):
        print(f'Depth: {state.depth}')
        print_board(state.board)

def get_actions(state: PuzzleState) -> list[str]:
    actions = []

    # remonte les parents
    while state.parent:
        dx = state.x - state.parent.x
        dy = state.y - state.parent.y

        # ajoute l'action à la liste
        actions.append(ACTION[(dx, dy)])

        # jusqu'à l'état parent
        state = state.parent
    
    # pour avoir les actions dans l'ordre de départ à l'arrivée
    actions.reverse()  
    return actions
