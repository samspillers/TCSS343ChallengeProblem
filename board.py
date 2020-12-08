class Board:
    def __init__(self, n: int, d: int):
        self.queens = []
        self.n = n
        self.d = d

    def valid_cell(self, location: tuple) -> bool:
        assert len(location) is self.d
        for index in location:
            assert 0 <= index < self.n

        for queen in self.queens:
            result = self.__check_vector(queen, location, tuple())
            if not result:
                return False
        return True

    def __check_vector(self, queen_1: tuple, queen_2: tuple, vector_thus_far: tuple) -> bool:
        if len(vector_thus_far) is self.d:
            for s in range(1, self.n):
                if queen_1 == tuple(queen_2[i] + s * vector_thus_far[i] for i in range(self.d)):
                    return False
            return True
        else:
            return self.__check_vector(queen_1, queen_2, vector_thus_far + (1,)) and self.__check_vector(queen_1, queen_2, vector_thus_far + (0,)) and self.__check_vector(queen_1, queen_2, vector_thus_far + (-1,))

    def add_queen(self, location: tuple):
        self.queens.append(location)

    def generate_board_array(self):
        board = self.__generate_board_array(self.d)
        for queen in self.queens:
            self.__set_position(board, queen)
        return board

    def __generate_board_array(self, d_remaining: int):
        if d_remaining is 1:
            return [False for _ in range(self.n)]
        else:
            return [self.__generate_board_array(d_remaining - 1) for _ in range(self.n)]

    def __set_position(self, board: list, location: tuple):
        if len(location) is 1:
            board[location[0]] = True
        else:
            self.__set_position(board[location[0]], location[1:len(location)])