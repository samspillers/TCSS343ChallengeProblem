import asyncio
import time

from algorithm import min_squares, brute_force
from board import Board

def example():
    board1 = Board(8, 2)
    board1.add_queen((1, 2))
    print("Checking valid cells on board1:")
    print(board1.valid_cell((0, 0)))
    print(board1.valid_cell((0, 3)))
    print(board1.valid_cell((4, 7)))
    print(board1.valid_cell((1, 5)))

    print()
    print("Checking valid cells on board2:")
    board2 = Board(3, 3)
    board2.add_queen((0, 0, 0))
    print(board2.valid_cell((0, 1, 2)))
    board2.add_queen((0, 1, 2))
    print(board2.valid_cell((1, 2, 0)))
    board2.add_queen((1, 2, 0))
    print(board2.valid_cell((2, 0, 1)))
    board2.add_queen((2, 0, 1))
    print("Printing queens on board2:")
    queens = board2.queens
    print(queens)

    print()
    print("Printing array representation of board3:")
    board3 = Board(8, 1)
    board3.add_queen((4,))
    board_array = board3.generate_board_array()
    print(board_array)

# async def async_function_test(the_function, output: list):
#     output.append(the_function())
#
# async def wait_15_minutes(output: list):
#     await asyncio.sleep(900)
#     output.append("Too long")

if __name__ == '__main__':
    print("Started...")
    n = 3
    d = 3
    output = []
    start_time = time.time()
    brute_force(n, d)
    print("n:", n, "d:", d, "Time:", time.time() - start_time)
