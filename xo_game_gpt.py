import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("X O Game")
        self.board = [" "] * 9
        self.current_player = "X"
        self.wins_player = 0
        self.wins_computer = 0

        self.create_buttons()

        reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=3, columnspan=3)

    def create_buttons(self):
        self.buttons = [
            [
                tk.Button(
                    self.master,
                    text=" ",
                    font=("normal", 20),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                for j in range(3)
            ]
            for i in range(3)
        ]

        for i, row_buttons in enumerate(self.buttons):
            for j, button in enumerate(row_buttons):
                button.grid(row=i, column=j)

    def on_button_click(self, i, j):
        if self.board[i * 3 + j] == " ":
            self.board[i * 3 + j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                winner = "Player" if self.current_player == "X" else "Computer"
                self.wins_player += 1 if self.current_player == "X" else 0
                self.wins_computer += 1 if self.current_player == "O" else 0
                self.show_winner_message(f"{winner} wins!", "green" if winner == "Player" else "red")
                self.highlight_winning_line('yellow' if winner == "Player" else 'red')
                self.reset_game()
            elif " " not in self.board:
                self.show_draw_message()
                self.reset_game()
            else:
                self.switch_player()
                if self.current_player == "O":
                    self.computer_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        empty_cells = [i for i, val in enumerate(self.board) if val == " "]
        if empty_cells:
            move = random.choice(empty_cells)
            self.board[move] = "O"
            i, j = divmod(move, 3)
            self.buttons[i][j].config(text="O")
            if self.check_winner():
                self.wins_computer += 1
                self.show_winner_message("Computer wins!", "red")
                self.highlight_winning_line('red')
                self.reset_game()
            elif " " not in self.board:
                self.show_draw_message()
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):
        for line in [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def show_winner_message(self, message, color):
        tk.messagebox.showinfo("Game Over", message)
        self.update_score(color)

    def show_draw_message(self):
        tk.messagebox.showinfo("Game Over", "It's a draw!")
        self.update_score("black") 

    def highlight_winning_line(self, color):
        for line in [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                for index in line:
                    i, j = divmod(index, 3)
                    self.buttons[i][j].config(fg="black", bg=color)

    def update_score(self, color):
        self.master.title(f"Score - Player: {self.wins_player} | Computer: {self.wins_computer}")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(fg=color, bg="white")

    def reset_game(self):
        self.board = [" "] * 9
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", fg="black", bg="white")
        self.update_score("black")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
