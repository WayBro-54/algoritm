# https://www.codewars.com/kata/64c743cb0a2a00002856ff73/train/python

def switch_gravity(blocks):
    rows, cols = len(blocks), len(blocks[0])

    for c in range(cols):
        row_idx = rows - 1
        for r in range(rows - 1, -1, -1):
            if blocks[r][c] == "#":
                blocks[r][c] = "-"
                blocks[row_idx][c] = "#"
                row_idx -= 1

    return blocks


# https://www.codewars.com/kata/5592fc599a7f40adac0000a8/train/python

def sum_diagonals(matrix):
    i, j = 0, len(matrix[0]) - 1
    res = 0
    for row in matrix:
        res += row[i] + row[j]
        i += 1
        j -= 1
    return res

# https://www.codewars.com/kata/6347f9715467f0001b434936/train/python

def thin_or_fat(matrix):
    row, cols = len(matrix), len(matrix[0])

    row_sum = [sum(i) for i in matrix]

# https://www.codewars.com/kata/60576b180aef19001bce494d/train/python

def count_checkerboard(width, height, resolution):
    count_full_cub = width * height // resolution**2
    res = 0
    if count_full_cub % 2 != 0 and (width * height) % resolution != 0:
        res += (width * height) % resolution
    res += (count_full_cub // 2) * resolution
    return count_full_cub

# print(count_checkerboard(9, 5, 8))

# https://www.codewars.com/kata/559656796d8fb52e17000003/train/python
# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python
def transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    transposed_matrix = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = arr[i][j]

    return transposed_matrix
# return [list(i) for i in zip(*arr)]
# print(transpose([[1,2,3],[4,5,6]]))

# https://www.codewars.com/kata/526233aefd4764272800036f/train/python

def matrix_addition(a, b):
    ab_row, ab_cols = len(a), len(a[0])

    for i in range(ab_row):
        for j in range(ab_cols):
            a[i][j] += b[i][j]
    return a