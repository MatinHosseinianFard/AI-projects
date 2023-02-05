import copy
from queue import Queue as PQueue
number_of_node = 0
n = 3

# bottom, left, top, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]


class Queue:

    def __init__(self):
        self.queue = PQueue()

    def push(self, k):
        self.queue.put(k)

    def pop(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()


class node:

    def __init__(self, parent, mat, empty_tile_pos, move="NOP"):

        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos

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


def newNode(mat, empty_tile_pos, new_empty_tile_pos, parent, final, move) -> node:

    new_mat = copy.deepcopy(mat)

    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    new_node = node(parent, new_mat, new_empty_tile_pos, move)
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


def EightPuzzle_BFS(initial, empty_tile_pos, final):

    q = Queue()

    root = node(None, initial, empty_tile_pos)
    q.push(root)

    while not q.empty():

        popNode = q.pop()
        if popNode.mat == final:

            printPath(popNode)
            global number_of_node
            print("Number of node : ", number_of_node, "\n")
            return

        for i in range(4):
            new_tile_pos = [
                popNode.empty_tile_pos[0] + row[i],
                popNode.empty_tile_pos[1] + col[i], ]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):

                child = newNode(popNode.mat,
                                popNode.empty_tile_pos,
                                new_tile_pos,
                                popNode, final, i)

                number_of_node += 1
                q.push(child)
