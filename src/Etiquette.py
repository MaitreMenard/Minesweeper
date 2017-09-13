import tkinter as tk

class Etiquette(tk.Label):
    colors = ["blue", "blue", "forest green", "orange red", "navy", "brown", "light sea green", "black", "gray", "black"]
    texts = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "x"]
    
    def __init__(self, minesweeper, i, j, number):
        super().__init__(minesweeper.cadre2, text = Etiquette.texts[number], fg = Etiquette.colors[number])
        self.minesweeper = minesweeper
        self.row = i
        self.column = j
        self.number = number
        self.bind("<Button-1>", self.leftClick)
        
    def leftClick(self, event):
        nbrFlags = 0
        for i in range(3):
            row = self.row + i - 1
            for j in range(3):
                column = self.column + j - 1
                if((row != self.row or column != self.column) and row >= 0 and row < self.minesweeper.height and column >= 0 and column < self.minesweeper.width):
                    if(self.minesweeper.liste_bouttons[row][column].clicked == False and self.minesweeper.liste_bouttons[row][column].flagged == True):
                        nbrFlags += 1
        if(nbrFlags == self.number):
            for i in range(3):
                row = self.row + i - 1
                for j in range(3):
                    column = self.column + j - 1
                    if((row != self.row or column != self.column) and row >= 0 and row < self.minesweeper.height and column >= 0 and column < self.minesweeper.width):
                        if(self.minesweeper.liste_bouttons[row][column].clicked == False and self.minesweeper.liste_bouttons[row][column].flagged == False):
                            self.minesweeper.liste_bouttons[row][column].presserBoutton()