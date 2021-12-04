def main():
    inp = open('in').read()
    nums, boards = inp.split('\n\n', 1)

    nums = [int(n) for n in nums.split(',')]
    boards = generate_boards(boards)

    score = simulate_game(nums, boards)
    print(f'final score: {score}')


def generate_boards(boards):
    boards = boards.split('\n\n')
    for i in range(len(boards)):
        b = boards[i].splitlines()
        b = [x.split() for x in b]
        b = [[[int(x), 0] for x in row] for row in b]
        boards[i] = b
    
    return boards


def simulate_game(nums, boards):
    for n in nums:
        print(f'{n=}')
        for board in boards:
            for row in board:
                for cell in row:
                    if cell[0] == n:
                        cell[1] = 1
                        if has_won(board):
                            s = get_sum_of_unmarked_numbers(board)
                            return s * n

                            
def has_won(board):
    for row in board:
        if all(cell[1] == 1 for cell in row):
            print('full row')
            print_board(board)
            return True

    for i in range(len(board[0])):
        column = [x[i] for x in board]
        if all(cell[1] == 1 for cell in column):
            print('full column')
            print_board(board)
            return True

    return False


def get_sum_of_unmarked_numbers(board):
    res = 0
    for row in board:
        for cell in row:
            if cell[1] == 0:
                res += cell[0]

    return res


def print_board(board):
    for row in board:
        print(row)


def print_boards(boards):
    for b in boards:
        for row in b:
            print(row)
        print()


main()