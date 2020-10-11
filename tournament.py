import random


class Tournament:
    def __init__(self, size, winning_strike=5):
        self.size = size
        self.winning_strike = winning_strike
        self.board = [[' ' for _ in range(size)] for i in range(size)]

    def print_board(self):
        template_lst = [''] + ['{:^3}' for _ in range(self.size)] + ['']
        template = '|'.join(template_lst)
        print('   -' + '---'.join([str(idx) for idx in range(self.size)]))  # for one square
        for idx, line in enumerate(self.board):
            print(f"{idx} " + template.format(*line))
            print('   -' + '-' * self.size * 4)

    def move(self, sym, row, column):
        if row < 0 or row >= self.size or column < 0 or column >= self.size:
            print("Out of board")
            return False
        if self.board[row][column] != ' ':
            return False
        self.board[row][column] = sym
        return True

    def is_over(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.board[row][column] == ' ':
                    return False
        return True

    def has_won(self, sym, row=None, column=None):
        # OPTIMIZED BUT NOT FINISHED
        # left_boundary = column - self.winning_strike if column - self.winning_strike < 0 else 0
        # right_boundary = column + self.winning_strike if column + self.winning_strike < self.size else self.size
        # upper_boundary = row - self.winning_strike if column - self.winning_strike < 0 else 0
        # lower_boundary = row + self.winning_strike if row + self.winning_strike < self.size else self.size
        #
        # left_upper_dia_boundary = left_boundary + upper_boundary
        # left_lower_dia_boundary = left_boundary + lower_boundary
        # right_upper_dia_boundary = left_boundary + upper_boundary
        # right_lower_dia_boundary = left_boundary + upper_boundary

        def check_row(sym, row, column, board, winning_strike):
            if row + winning_strike > len(board):
                return False
            for r in range(row, row + winning_strike):
                if board[r][column] != sym:
                    return False
            return True

        def check_column(sym, row, column, board, winning_strike):
            if column + winning_strike > len(board):
                return False
            for c in range(column, column + winning_strike):
                if board[row][c] != sym:
                    return False
            return True

        def check_diagonal(sym, row, column, board, winning_strike):
            if column + winning_strike > len(board) or row + winning_strike > len(board):
                return False
            for c, r in zip(range(column, column + winning_strike), range(row, row + winning_strike)):
                if board[r][c] != sym:
                    return False
            return True

        for row in range(0, self.size):
            for column in range(0, self.size):
                if check_row(sym, row, column, self.board, self.winning_strike) or \
                        check_column(sym, row, column, self.board, self.winning_strike) or \
                        check_diagonal(sym, row, column, self.board, self.winning_strike):
                    return True
        return False


class Player:
    def __init__(self, sym):
        self.sym = sym

    def play(self):  # return tuple (row, column)
        return self.sym, random.randint(0, 7), random.randint(0, 7)


def play(tournament: Tournament, player1: Player, player2: Player):
    while not tournament.is_over():
        for pl in [player1, player2]:
            while True:
                sym, row, column = pl.play()
                if tournament.move(sym, row, column):
                    break
                else:
                    print(f"Not valid move for {sym} at r:{row}/c:{column}")

            if tournament.has_won(sym, row, column):
                print(f"{sym} has won")
                trn.print_board()
                return
            if tournament.is_over():
                print("It is tie!")
                trn.print_board()
                return
        trn.print_board()


trn = Tournament(8)
trn.move("x", 0, 0)
trn.move("x", 1, 1)
trn.move("x", 2, 2)
trn.move("x", 3, 3)
print(trn.has_won("x"))
print(trn.has_won("o"))
trn.move("x", 5, 5)
print(trn.has_won("x"))
print(trn.has_won("o"))
trn.move("x", 4, 4)
print(trn.has_won("x"))
print(trn.has_won("o"))
trn.print_board()

print()
print()
print()
trn = Tournament(8)
player1 = Player("x")
player2 = Player("O")
play(trn, player1, player2)
