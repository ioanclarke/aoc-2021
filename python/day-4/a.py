def main():
    inp = open('in').read()
    nums, boards = inp.split('\n\n', 1)

    nums = [int(n) for n in nums.split(',')]
    boards = generate_boards(boards)

    winning_board, last_number_called = find_winning_board_and_last_number(nums, boards)
    score = get_sum_of_unmarked_numbers(winning_board) * last_number_called
    print(f'final score: {score}')


def generate_boards(boards_str):
    boards = boards_str.split('\n\n')
    for i in range(len(boards)):
        board = boards[i].splitlines()
        board_as_grid = [x.split() for x in board]
        board_as_grid_with_marked_indicator = [[[int(x), 0] for x in row] for row in board_as_grid]
        boards[i] = board_as_grid_with_marked_indicator
    
    return boards


def find_winning_board_and_last_number(nums, boards):
    for n in nums:
        for board in boards:
            for row in board:
                for cell in row:
                    if cell[0] == n:
                        cell[1] = 1
                        if has_won(board):
                            return board, n


def has_won(board):
    def has_complete_row(board):
        for row in board:
            if all(cell[1] == 1 for cell in row):
                return True
                
        return False

    def has_complete_column(board):
        for i in range(len(board[0])):
            column = [x[i] for x in board]
            if all(cell[1] == 1 for cell in column):
                return True

        return False

    return has_complete_row(board) or has_complete_column(board)                            


def get_sum_of_unmarked_numbers(board):
    return sum(cell[0] for row in board for cell in row if cell[1] == 0)


main()