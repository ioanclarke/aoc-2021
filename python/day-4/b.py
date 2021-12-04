def main():
    inp = open('in').read()
    nums, boards = inp.split('\n\n', 1)

    nums = [int(n) for n in nums.split(',')]
    boards = generate_boards(boards)

    losing_board, last_number_called = find_losing_board_and_last_number(nums, boards)
    
    score = get_sum_of_unmarked_numbers(losing_board) * last_number_called
    print(f'final score: {score}')
    




def find_losing_board_and_last_number(nums, boards):
    for n in nums:
        remaining_boards = []
        for board in boards:
            for row in board:
                for cell in row:
                    if cell[0] == n:
                        cell[1] = 1
            if not has_won(board):
                remaining_boards.append(board)
            elif len(boards) == 1:
                return boards[0], n
        boards = remaining_boards
                            
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