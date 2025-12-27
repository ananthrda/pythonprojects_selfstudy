from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        # we wil use a single list to rep3*3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner!

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        # 0|1|2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('|' + '|'.join(row) + '|')

    def availbale_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere,check row,column and diagnol
        row_index = square // 3
        row = self.board[row_index*3: (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check col ind
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagnols
        if square % 2 == 0:
            diagnol1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagnol1]):
                return True
            diagnol2 = [self.board[i] for i in [2, 4, 8]]
            if all([spot == letter for spot in diagnol2]):
                return True

        # if all the checks fail
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + 'wins')
                return letter

            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
