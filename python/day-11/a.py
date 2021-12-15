from typing import List, Tuple

def main():
    inp = open('in').read().split()

    energies = [list(map(int, list(row))) for row in inp]
    print('Before any steps')
    p(energies)

    flashes = simulate(energies, 100)

    print(flashes)


def simulate(energies: List[List[int]], steps: int) -> int:
    flashes = 0
    for _ in range(steps):
        energies = increase(energies)
        flashes += num_of_flashes(energies)
        energies = reset(energies)
        # print(f'After step {i + 1}')
        # p(energies)
    return flashes


def increase(energies: List[List[int]]) -> List[List[int]]:
    return [[x + 1 for x in row] for row in energies]


def num_of_flashes(energies: List[List[int]]) -> int:
    flashes = 0
    flashed: List[Tuple] = []

    while True:
        flashers = find_flashers(energies, flashed)
        if len(flashers) == 0:
            break
        flashes += len(flashers)
        for row_num, cell_num in flashers:
            increase_adjacent_energies(energies, row_num, cell_num)
        flashed.extend(flashers)
        p(energies)
    return flashes



def find_flashers(energies, flashed):
    flashers = []
    for row_num, row in enumerate(energies):
        for cell_num, cell in enumerate(row):
            if cell >= 10 and (row_num, cell_num) not in flashed:
                flashers.append((row_num, cell_num))
    return flashers


def reset(energies: List[List[int]]) -> List[List[int]]:
    return [[x if x <= 9 else 0 for x in row] for row in energies]

def increase_adjacent_energies(energies: List[List[int]], row_num: int, cell_num: int):
    num_of_rows = len(energies)
    row_length = len(energies[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            curr_row_num = row_num + i
            curr_cell_num = cell_num + j
            if 0 <= curr_row_num < num_of_rows and 0 <= curr_cell_num < row_length and not i==j==0:
                energies[curr_row_num][curr_cell_num] += 1


def p(energies):
    for row in energies:
        print(row)
    print()
main()
