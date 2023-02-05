import numpy as np


def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def isSolvable(puzzle):

    inv_count = getInvCount([j for sub in puzzle for j in sub])

    return (inv_count % 2 == 0)


def generate():
    while True:
        initial = np.random.choice(9, size=(3, 3), replace=False).tolist()
        if (isSolvable(initial)):
            for i, x in enumerate(initial):
                if 0 in x:
                    j = x.index(0)
                    return initial, [i, j]