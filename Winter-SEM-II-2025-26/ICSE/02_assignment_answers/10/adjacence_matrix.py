from typing import List


def in_degree(k: int, m: List[List[int]]) -> int:
    degree = 0
    for i in m:
        if i[k] != 0:
            degree += 1
    return degree


def out_degree(k: int, m: List[List[int]]) -> int:
    degree = 0
    for i in m[k]:
        if i != 0:
            degree += 1
    return degree


def adjacent(k: int, m: List[List[int]]) -> List[int]:
    adjacent_nodes = []
    row = m[k]
    for j in range(0, len(row)):
        if row[j] != 0:
            adjacent_nodes.append(j)
    return adjacent_nodes


def has_triangle(m: List[List[int]]) -> bool:
    final = []
    intermediate = []
    A = m
    B = m
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(A[0])):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        intermediate.append(row)
    for i in range(len(intermediate)):
        new_row = []
        for j in range(len(B[0])):
            sum_val_2 = 0
            for k in range(len(intermediate[0])):
                sum_val_2 += intermediate[i][k] * B[k][j]
            new_row.append(sum_val_2)
        final.append(new_row)

    principal = 0
    for i in range(0, len(final)):
        principal += final[i][i]

    if principal > 0:
        return True

    return False


if __name__ == "__main__":
    inner = [0, 1, 1]
    inner2 = [0, 1, 1]
    inner3 = [1, 0, 1]
    outer = []
    outer.append(inner)
    outer.append(inner2)
    outer.append(inner3)
    print('in-degree: ', in_degree(0, outer))
    print('out-degree: ', out_degree(1, outer))
    print('adjacency of 1: ', adjacent(1, outer))
    assert in_degree(2, outer) == 3
    assert out_degree(1, outer) == 2
    assert adjacent(1, outer) == [1, 2]
    assert has_triangle(outer)
