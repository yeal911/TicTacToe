from tkinter import *
from TicTacToe.Board import Board

tk = Tk()
tk.title("TicTacToe")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
game_canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0)
game_canvas.configure(bg='white')
game_canvas.pack()
tk.update()
board = Board(game_canvas)
board.draw()
game_canvas.mainloop()


