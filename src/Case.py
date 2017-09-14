import tkinter as tk


class Case(tk.Button):
    def __init__(self, minesweeper, i, j, text):
        super().__init__(minesweeper.cadre2, command=self.presserBoutton, text=text)
        self.minesweeper = minesweeper
        self.i = i
        self.j = j
        self.clicked = False
        self.flagged = False
        self.bind("<Button-3>", self.rightClick)        
    
    def presserBoutton(self):
        if not self.minesweeper.started:
            self.minesweeper.started = True
            print("game start : " + str(self.minesweeper.started))
        self.clicked = True
        if self.minesweeper.field.has_mine_at_position(self.i, self.j):
            self.destroy()
            print("BOOM !!!!")
            self.minesweeper.vivant = False
        elif self.minesweeper.field[self.i, self.j] == 0:
            if self.i-1 >= 0 and self.j-1 >= 0 and not self.minesweeper.is_clicked(self.i-1, self.j-1):
                self.minesweeper.liste_bouttons[self.i-1][self.j-1].presserBoutton()

            if self.i-1 >= 0 and not self.minesweeper.is_clicked(self.i-1, self.j):
                self.minesweeper.liste_bouttons[self.i-1][self.j].presserBoutton()

            if self.i-1 >= 0 and self.j+1 < self.minesweeper.width and not self.minesweeper.is_clicked(self.i-1, self.j+1):
                self.minesweeper.liste_bouttons[self.i-1][self.j+1].presserBoutton()

            if self.j-1 >= 0 and not self.minesweeper.is_clicked(self.i, self.j-1):
                self.minesweeper.liste_bouttons[self.i][self.j-1].presserBoutton()

            if self.j+1 < self.minesweeper.width and not self.minesweeper.is_clicked(self.i, self.j+1):
                self.minesweeper.liste_bouttons[self.i][self.j+1].presserBoutton()

            if self.i+1 < self.minesweeper.height and self.j-1 >= 0 and not self.minesweeper.is_clicked(self.i+1, self.j-1):
                self.minesweeper.liste_bouttons[self.i+1][self.j-1].presserBoutton()

            if self.i+1 < self.minesweeper.height and not self.minesweeper.is_clicked(self.i+1, self.j):
                self.minesweeper.liste_bouttons[self.i+1][self.j].presserBoutton()

            if self.i+1 < self.minesweeper.height and self.j+1 < self.minesweeper.width and not self.minesweeper.is_clicked(self.i+1, self.j+1):
                self.minesweeper.liste_bouttons[self.i+1][self.j+1].presserBoutton()
        self.destroy()
        self.minesweeper.nbrBouttons -= 1
        #print(self.minesweeper.nbrBouttons)
        if self.minesweeper.nbrBouttons == self.minesweeper.nbrMines:
            self.minesweeper.win = True
        
    def rightClick(self, event):
        if self["text"] == "    ":
            self["text"] = "  ! "
            self["foreground"] = "red"
            self.flagged = True
            if self.minesweeper.minesLeft > 0:
                self.minesweeper.minesLeft -= 1
        elif self["text"] == "  ! ":
            self["text"] = " ? "
            self["foreground"] = "black"
            self.flagged = False
            self.minesweeper.minesLeft += 1
        elif self["text"] == " ? ":
            self["text"] = "    "
        self.minesweeper.updateLabel_MinesLeft()
