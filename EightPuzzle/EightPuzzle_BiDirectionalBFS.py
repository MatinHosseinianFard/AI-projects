from queue import Queue as PQueue
import copy
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


def printPath(intersecting_node_from_src, intersecting_node_from_dest, src, dest):
    path = list()
    src_move = list()
    dest_move = list()
    path.append(intersecting_node_from_src)
    i = intersecting_node_from_src

    while i.mat != src.mat and i.parent:
        path.append(i.parent)
        src_move.append(i.move)
        i = i.parent
    path = path[::-1]
    src_move.reverse()
    i = intersecting_node_from_dest

    while i.mat != dest.mat and i.parent:
        if i.move == "left":
            i.move = "right"
        elif i.move == "right":
            i.move = "left"
        elif i.move == "top":
            i.move = "bottom"
        elif i.move == "bottom":
            i.move = "top"
        path.append(i.parent)
        dest_move.append(i.move)
        i = i.parent
    # dest_move.reverse()
    src_move.extend(dest_move)
    src_move.insert(0, "NOP")
    for i, node in enumerate(path):
        print("-->", src_move[i])
        printMatrix(node.mat)

def is_intersecting(src_visited, dest_visited):

    lst = [value for value in src_visited if value in dest_visited]
    if any(lst):
        return lst[0]
    else:
        return -1


def EightPuzzle_BiDirectionalBFS(initial, empty_tile_pos, final):
    global number_of_node
    src_q = Queue()
    dest_q = Queue()

    src_visited_node = []
    src_visited_mat = []
    dest_visited_node = []
    dest_visited_mat = []

    src = node(None, initial, empty_tile_pos)
    src_q.push(src)
    src_visited_node.append(src)
    src_visited_mat.append(src.mat)

    dest = node(None, final, [2, 2])
    dest_q.push(dest)
    dest_visited_node.append(dest)
    dest_visited_mat.append(dest.mat)

    while src_q and dest_q:

        src_popNode = src_q.pop()

        for i in range(4):
            new_tile_pos = [
                src_popNode.empty_tile_pos[0] + row[i],
                src_popNode.empty_tile_pos[1] + col[i], ]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):

                child = newNode(src_popNode.mat,
                                src_popNode.empty_tile_pos,
                                new_tile_pos,
                                src_popNode, final, i)
                if child.mat in src_visited_mat:
                    continue
                src_visited_node.append(child)
                src_visited_mat.append(child.mat)
                number_of_node += 1
                src_q.push(child)

        dest_popNode = dest_q.pop()

        for i in range(4):
            new_tile_pos = [
                dest_popNode.empty_tile_pos[0] + row[i],
                dest_popNode.empty_tile_pos[1] + col[i], ]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):

                child = newNode(dest_popNode.mat,
                                dest_popNode.empty_tile_pos,
                                new_tile_pos,
                                dest_popNode, initial, i)
                if child.mat in dest_visited_mat:
                    continue
                dest_visited_node.append(child)
                dest_visited_mat.append(child.mat)
                number_of_node += 1
                dest_q.push(child)

        intersecting_mat = is_intersecting(src_visited_mat, dest_visited_mat)
        if intersecting_mat != -1:
            intersecting_node_from_src = src_visited_node[src_visited_mat.index(
                intersecting_mat)]
            intersecting_node_from_dest = dest_visited_node[dest_visited_mat.index(
                intersecting_mat)]
            printPath(intersecting_node_from_src,
                      intersecting_node_from_dest, src, dest)
            print("\nNumber of node : ", number_of_node, "\n")
            
            return
