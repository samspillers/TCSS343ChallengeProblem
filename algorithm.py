from board import Board


def brute_force(n: int, d: int):
    return __brute_force(n, d, tuple(), Board(n, d))

def __brute_force(n: int, d: int, index: tuple, board: Board) -> list:
    if len(index) is d:
        if __board_full(board):
            return board.queens.copy()
        else:
            if board.valid_cell(index):
                board.add_queen(index)
                result = __brute_force(n, d, tuple(), board)
                board.remove_queen(index)
                return result
            else:
                return []
    else:
        output = None
        outputs = []
        for i in range(n):
            current_output = __brute_force(n, d, index + (i,), board)
            outputs += current_output
            if output is None or len(current_output) > len(output):
                output = current_output
        return output

def __board_full(board: Board):
    output = True
    for index in get_list_of_all_indexes(board.n, board.d):
        output = output and not board.valid_cell(index)
    return output


def min_squares(n: int, d: int):
    board = Board(n, d)
    working_set = get_list_of_all_indexes(n, d)
    print(working_set)
    while len(working_set) is not 0:
        previously_dead_cells = count_dead_squares(n, d, board)
        queen_count = {}
        for queen in working_set:
            board.add_queen(queen)
            queen_count[queen] = count_dead_squares(n, d, board) - previously_dead_cells
            board.remove_queen(queen)

        queen_to_add = get_centermost_queen(get_min_queens(queen_count), n, d, board)
        board.add_queen(queen_to_add)

        # Can't remove from current working set or iteration breaks
        next_working_set = working_set.copy()
        for index in working_set:
            if not board.valid_cell(index):
                next_working_set.remove(index)
        working_set = next_working_set
    return board

def count_dead_squares(n: int, d: int, board: Board):
    count = 0
    for index in get_list_of_all_indexes(n, d):
        if not board.valid_cell(index):
            count += 1
    return count

def get_min_queens(queen_count: dict):
    min_queens = []
    for queen in queen_count.keys():
        if len(min_queens) is 0 or queen_count[queen] < queen_count[min_queens[0]]:
            min_queens.clear()
            min_queens.append(queen)
        elif queen_count[queen] == queen_count[min_queens[0]]:
            min_queens.append(queen)
    return min_queens

def get_clumped_or_center_queen(queens: list, n: int, d: int, board: Board):
    center = tuple(float(n) / 2 for _ in range(d))
    min_queen = None
    min_distance = None
    for queen in queens:
        if len(board.queens) is not 0:
            distance = distance_to_other_queens(queen, board)
        else:
            distance = distance_between(center, queen) * -1
        if min_queen is None or min_distance is None or distance < min_distance:
            min_queen = queen
            min_distance = distance
    return min_queen

def distance_to_other_queens(queen: tuple, board: Board) -> float:
    distance = 0
    for current_queen in board.queens:
        distance += distance_between(queen, current_queen)
    return distance

def distance_between(point1: tuple, point2: tuple):
    return sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))]) ** 1 / 2

def get_list_of_all_indexes(n: int, d: int):
    return __get_list_of_all_indexes(n, d, tuple())

def __get_list_of_all_indexes(n: int, d: int, done_indexes: tuple) -> list:
    if d is 1:
        return [done_indexes + (i,) for i in range(n)]
    else:
        output = []
        for i in range(n):
            output.extend(__get_list_of_all_indexes(n, d - 1, done_indexes + (i,)))
        return output

