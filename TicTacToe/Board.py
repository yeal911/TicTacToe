from tkinter import Canvas, ttk

from TicTacToe.Piece import Piece

import random


class Board:
    def __init__(self, canvas: Canvas):
        a: list = ["X", "O"]
        self.array = [[""] * 3 for i in range(3)]
        self.gap = 200
        self.canMove = True
        self.turn = a[random.randint(0, 1)]
        self.color = 'black'
        self.canvas = canvas
        self.canvas.bind("<Button-1>", self.place_piece)

    def draw(self):
        for i in range(1, 3):
            # draw rows
            self.canvas.create_line(0, self.gap * i, 3 * self.gap, self.gap * i, fill=self.color, width=4)
            # draw cols
            self.canvas.create_line(self.gap * i, 0, self.gap * i, 3 * self.gap, fill='black', width=4)
            self.canvas.update()
            button = ttk.Button(self.canvas, text="Restart", command=self.restart)
            self.canvas.create_window(self.gap * 3.5, self.gap // 2, window=button)

    def place_piece(self, event):
        if self.canMove:
            row = event.y // self.gap
            col = event.x // self.gap
            piece1 = Piece(self.turn, row, col)
            color = "green"
            if self.turn == "O":
                color = "blue"
            if self.array[piece1.row][piece1.col] == "":
                self.canvas.create_text(piece1.col * self.gap + self.gap // 2, piece1.row * self.gap + self.gap // 2, text=piece1.piece_type, fill=color,
                                        font='Helvetica 30')
                self.array[piece1.row][piece1.col] = piece1.piece_type
                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"
            if self.check_win(piece1):
                self.canvas.create_text(self.gap * 3 // 2, self.gap * 3 // 2, text=piece1.piece_type + " wins!", font="Helvetica 40", fill="red")
                self.canMove = False
            elif self.check_tie():
                self.canvas.create_text(self.gap * 3 // 2, self.gap * 3 // 2, text="Tie!",
                                        font="Helvetica 40", fill="red")

    def check_win(self, piece: Piece):
        win_counter:int = 1
        # check left
        for i in range(1, 4):
            if (piece.col - i) >= 0 and self.array[piece.row][piece.col - i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True
        # check right
        for i in range(1, 4):
            if (piece.col + i) <= 2 and self.array[piece.row][piece.col + i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True
        # Check vertical
        win_counter = 1
        # check up
        for i in range(1, 4):
            if (piece.row - i) >= 0 and self.array[piece.row - i][piece.col] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True
        # check down
        for i in range(1, 4):
            if (piece.row + i) <= 2 and self.array[piece.row + i][piece.col] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True

        win_counter = 1
        # check up + left
        for i in range(1, 4):
            if (piece.row - i) >= 0 and (piece.col - i) >= 0 and self.array[piece.row - i][piece.col - i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 5:
            return True
        # check down + right
        for i in range(1, 5):
            if (piece.row + i) <= 2 and (piece.col + i) <= 2 and self.array[piece.row + i][piece.col + i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True

        win_counter = 1
        # check up + right
        for i in range(1, 5):
            if (piece.row - i) >= 0 and (piece.col + i) <= 2 and self.array[piece.row - i][piece.col + i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True
        # check down + left
        for i in range(1, 4):
            if (piece.row + i) <= 2 and (piece.col - i) >= 0 and self.array[piece.row + i][piece.col - i] == piece.piece_type:
                win_counter += 1
            else:
                break
        if win_counter >= 3:
            return True

    def check_tie(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.array[i][j] == "":
                    return False
        return True

    def restart(self):
        self.canvas.delete("all")
        self.array = [[""] * 3 for i in range(3)]
        self.canMove = True
        self.draw()

