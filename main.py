
import numpy as np

puzzle = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
          [0, 1, 0, 0, 0, 4, 0, 0, 0],
          [4, 0, 7, 0, 0, 0, 2, 0, 8],
          [0, 0, 5, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 9, 8, 1, 0, 0],
          [0, 4, 0, 0, 0, 3, 0, 0, 0],
          [0, 0, 0, 3, 6, 0, 0, 7, 2],
          [0, 7, 0, 0, 0, 0, 0, 0, 3],
          [9, 0, 3, 0, 0, 0, 6, 0, 4]]

solved_puzzle = puzzle
print(np.matrix(puzzle))



def get_row(pos):

    return puzzle[pos // 9]


def get_col(pos):
    result = []
    for i in range(9):
        result.append(puzzle[i][pos % 9])
    return result

def get_box(pos):
    result = []
    box_col = (pos % 9) // 3 * 3
    box_row = pos // 9 // 3 * 3
    for i in range(3):
        result.append(puzzle[box_row + 0][box_col + i])
        result.append(puzzle[box_row + 1][box_col + i])
        result.append(puzzle[box_row + 2][box_col + i])
    return result

def check_pos(pos, num):
       result = []
       result += get_row(pos)
       result += get_col(pos)
       result += get_box(pos)
       return num not in result


def solve():
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                for i in range(1, 10):
                    pos = r * 9 + c
                    if check_pos(pos, i):
                        puzzle[r][c] = i
                        solve()
                    puzzle[r][c] = 0
                return
    print(np.matrix(puzzle))

solve()
