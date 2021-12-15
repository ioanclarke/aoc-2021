def main():
    grid = [[int(x) for x in row] for row in open('in').read().split()]
    print(sum(cell + 1 for row_num, row in enumerate(grid) for cell_num, cell in enumerate(row) if low_point(cell_num, cell, row_num, grid)))


def low_point(cell_num, cell, row_num, grid):
    # conds = [
    #     cell_num != 0 and grid[row_num][cell_num - 1] < cell,
    #     cell_num != len(grid[0]) - 1 and grid[row_num][cell_num + 1] < cell,
    #     row_num != 0 and grid[row_num - 1][cell_num] < cell,
    #     row_num != len(grid) - 1 and grid[row_num + 1][cell_num] < cell
    # ]


    # print(f'{cell=}')
    # for i, cond in enumerate(conds):
    #     if cond:
    #         print(f'cond {i} is true')
    #         print()
    #         return False

    # print('No cond true')
    # print()
    # return True
    # return not any(cond for cond in conds)
    neighbours = []
    if cell_num != 0:
        neighbours.append(grid[row_num][cell_num - 1])

    if cell_num != len(grid[0]) - 1:
        neighbours.append(grid[row_num][cell_num + 1])

    if row_num != 0:
        neighbours.append(grid[row_num - 1][cell_num])

    if row_num != len(grid) - 1:
        neighbours.append(grid[row_num + 1][cell_num])

    # print(neighbours)
    # print()
    return all(x > cell for x in neighbours)


main()