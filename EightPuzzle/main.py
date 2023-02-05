import time

from EightPuzzle_AStar import EightPuzzle_AStar, calculateCost, calculateCostManhattan, printMatrix
from EightPuzzle_BFS import EightPuzzle_BFS
from EightPuzzle_BiDirectionalBFS import EightPuzzle_BiDirectionalBFS

from solvable_puzzle_generate import generate


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


final = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]

initial, empty_tile_pos = generate()

while True:
    print(style.GREEN + "\n--------------------------------------" + style.RESET)
    print("initial board : ")
    printMatrix(initial)
    print("\nAlgorithms for solve:\n1) A* (Manhattan Distance heuristic)\n2) A* (non-blank tiles not in their goal position heuristic)\n3) Bi-directional(BFS variant)\n4) BFS (non heuristic)\n5) New initial board\n6) Exit ")
    choosed = int(input("Choose : "))

    if choosed == 1:
        st = time.time()
        EightPuzzle_AStar(initial, empty_tile_pos,
                          final, calculateCostManhattan)
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', round(elapsed_time, 4), 'seconds')
    elif choosed == 2:
        st = time.time()
        EightPuzzle_AStar(initial, empty_tile_pos, final, calculateCost)
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', round(elapsed_time, 4), 'seconds')
    elif choosed == 3:
        st = time.time()
        EightPuzzle_BiDirectionalBFS(initial, empty_tile_pos, final)
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', round(elapsed_time, 4), 'seconds')
    elif choosed == 4:
        st = time.time()
        EightPuzzle_BFS(initial, empty_tile_pos, final)
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', round(elapsed_time, 4), 'seconds')
    elif choosed == 5:
        initial, empty_tile_pos = generate()
    elif choosed == 6:
        break
    print(style.GREEN + "--------------------------------------" + style.RESET)