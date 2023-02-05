from heapq import heappush, heappop
import copy
import time
number_of_node = 0
n = 3

# bottom, left, top, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]


class priorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class node:

    def __init__(self, parent, mat, empty_tile_pos,
                 cost, level, move="NOP"):

        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

        if move == 0:
            self.move = "top"
        elif move == 1:
            self.move = "right"
        elif move == 2:
            self.move = "bottom"
        elif move == 3:
            self.move = "left"
        else:
            self.move = move

    def __lt__(self, nxt):
        return self.cost + self.level < nxt.cost + nxt.level

    def __repr__(self):
        return str(self.mat)


def calculateCost(mat, final) -> int:

    count = 0
    for i in range(n):
        for j in range(n):
            if (mat[i][j] and (mat[i][j] != final[i][j])):
                count += 1

    return count


def calculateCostManhattan(mat, final) -> int:

    count = 0
    for i in range(n):
        for j in range(n):
            if (mat[i][j] and (mat[i][j] != final[i][j])):
                for i_goal, x in enumerate(final):
                    if mat[i][j] in x:
                        j_goal = x.index(mat[i][j])
                        count += abs(i_goal - i) + abs(j_goal - j)
                        break

    return count


def newNode(mat, empty_tile_pos, new_empty_tile_pos,
            level, parent, final, move, heuristic) -> node:

    new_mat = copy.deepcopy(mat)

    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    cost = heuristic(new_mat, final)

    new_node = node(parent, new_mat, new_empty_tile_pos,
                    cost, level, move)
    return new_node


def printMatrix(mat):

    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end=" ")

        print()


def isSafe(x, y):

    return x >= 0 and x < n and y >= 0 and y < n


def printPath(root):
    if root == None:
        return

    printPath(root.parent)
    print("-->", root.move)
    printMatrix(root.mat)


def EightPuzzle_AStar(initial, empty_tile_pos, final, heuristic):

    pq = priorityQueue()

    cost = heuristic(initial, final)
    root = node(None, initial,
                empty_tile_pos, cost, 0)

    pq.push(root)

    while not pq.empty():

        minimum = pq.pop()

        if minimum.cost == 0:

            printPath(minimum)
            global number_of_node
            print("\nNumber of node : ", number_of_node, "\n")
            return

        for i in range(4):
            new_tile_pos = [
                minimum.empty_tile_pos[0] + row[i],
                minimum.empty_tile_pos[1] + col[i], ]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):

                child = newNode(minimum.mat,
                                minimum.empty_tile_pos,
                                new_tile_pos,
                                minimum.level + 1,
                                minimum, final, i, heuristic)

                number_of_node += 1
                pq.push(child)

