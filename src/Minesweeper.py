import tkinter as tk
from field import Field
from Case import Case, ButtonState
from Etiquette import Etiquette
from Chrono import Chrono
from view.menu import Menu
from view.options_window import OptionsWindow
from view.statistics_window import StatisticsWindow
from view.header import Header


class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.nbrMines = mines
        self.minesLeft = mines
        self.chrono = None
        self.liste_bouttons = []

        self.root = tk.Tk()
        self.root.title('Minesweeper')
        self.menu = Menu(self.root, self.new_game, self.on_statistics_window_opened, self.on_options_window_opened,
                         self.exit)
        self.header = Header(self.root, self.new_game)

        self.cadre2 = tk.Frame(self.root, height=347, width=277)
        self.cadre2.grid(padx=6, pady=4)
        self.cadre2['relief'] = tk.SUNKEN
        self.cadre2["borderwidth"] = 5
        self.cadre2.grid_propagate(0)
        
        self.new_game()
        self.root.mainloop()
        #while self.vivant == True:
         #   self.root.update()
          #  self.updateLabel_Time()
        
    def new_game(self):
        self.vivant = True
        self.win = False
        self.started = False
        self.openfile()
        self.minesLeft = self.nbrMines
        self.nbrBouttons = self.width * self.height
        self.header.set_mines_left(self.minesLeft)
        if len(self.liste_bouttons) != 0:
            for i in range(self.height):
                for j in range(self.width):
                    self.liste_bouttons[i][j].destroy()
            self.liste_bouttons.clear()
        self.field = Field(self.height, self.width, self.nbrMines)
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if self.field.has_mine_at_position(i, j):
                    Etiquette(self.cadre2, i, j, -1, self.on_label_left_click)
                else:
                    Etiquette(self.cadre2, i, j, self.field[i, j], self.on_label_left_click)

                bt = Case(self.cadre2, i, j, self.on_button_tile_left_click, self.on_button_tile_right_click)
                row.append(bt)
            self.liste_bouttons.append(row)
        self.header.set_time(0)
        if self.chrono is None:
            self.chrono = Chrono()
        else:
            self.chrono.reset()
        self.root.after(1, self.update)
    
    def update(self):
        if self.vivant:
            if self.started:
                if not self.win:
                    self.header.set_time(int(self.chrono.get()))
                    self.root.after(1, self.update)
                else:
                    time = int(self.chrono.get())
                    ecrire_stats = open("stats.txt", "w")
                    if time < self.highScore:
                        ecrire_stats.write(str(time)+"\n")
                    else:
                        ecrire_stats.write(str(self.highScore)+"\n")
                    ecrire_stats.write(str(self.nbrGames)+"\n")
                    self.nbrWins += 1
                    ecrire_stats.write(str(self.nbrWins)+"\n")
                    ecrire_stats.close()
            else:
                self.root.after(1, self.update)
        
    def openfile(self):
        fich = open("stats.txt", "r")        
        liste = fich.readlines()
        fich.close()
        print(liste)
        #self.stats = {"easy":{}, "medium":{}, "hard":{}}
        self.highScore = int(liste[0])
        self.nbrGames = int(liste[1]) + 1
        self.nbrWins = int(liste[2])
        fich = open("stats.txt", "w")
        fich.write(str(self.highScore)+"\n")
        fich.write(str(self.nbrGames)+"\n")
        fich.write(str(self.nbrWins))
        fich.close()
        
    def on_statistics_window_opened(self):
        StatisticsWindow(self.nbrGames, self.nbrWins, self.highScore)
        
    def on_options_window_opened(self):
        OptionsWindow()

    def on_button_tile_left_click(self, i, j):
        if not self.started:
            self.started = True
            print("game start : " + str(self.started))
        if self.field.has_mine_at_position(i, j):
            print("BOOM !!!!")
            self.vivant = False
        elif self.field[i, j] == 0:
            if i-1 >= 0 and j-1 >= 0 and not self.is_clicked(i-1, j-1):
                self.liste_bouttons[i-1][j-1].on_left_click()
            if i-1 >= 0 and not self.is_clicked(i-1, j):
                self.liste_bouttons[i-1][j].on_left_click()
            if i-1 >= 0 and j+1 < self.width and not self.is_clicked(i-1, j+1):
                self.liste_bouttons[i-1][j+1].on_left_click()
            if j-1 >= 0 and not self.is_clicked(i, j-1):
                self.liste_bouttons[i][j-1].on_left_click()
            if j+1 < self.width and not self.is_clicked(i, j+1):
                self.liste_bouttons[i][j+1].on_left_click()
            if i+1 < self.height and j-1 >= 0 and not self.is_clicked(i+1, j-1):
                self.liste_bouttons[i+1][j-1].on_left_click()
            if i+1 < self.height and not self.is_clicked(i+1, j):
                self.liste_bouttons[i+1][j].on_left_click()
            if i+1 < self.height and j+1 < self.width and not self.is_clicked(i+1, j+1):
                self.liste_bouttons[i+1][j+1].on_left_click()
        self.nbrBouttons -= 1
        if self.nbrBouttons == self.nbrMines:
            self.win = True

    def on_button_tile_right_click(self, new_button_state):
        if new_button_state == ButtonState.FLAGGED:
            if self.minesLeft > 0:
                self.minesLeft -= 1
        elif new_button_state == ButtonState.NORMAL:
            self.minesLeft += 1
        self.header.set_mines_left(self.minesLeft)

    # TODO: rename this method
    def on_label_left_click(self, label_row, label_column):
        flags = 0
        for i in range(3):
            row = label_row + i - 1
            for j in range(3):
                column = label_column + j - 1
                if (row != label_row or column != label_column) and row >= 0 and row < self.height and column >= 0 and column < self.width:
                    if not self.is_clicked(row, column) and self.is_flagged(row, column):
                        flags += 1
        if flags == self.field[label_row, label_column]:
            for i in range(3):
                row = label_row + i - 1
                for j in range(3):
                    column = label_column + j - 1
                    if (row != label_row or column != label_column) and row >= 0 and row < self.height and column >= 0 and column < self.width:
                        if not self.is_clicked(row, column) and not self.is_flagged(row, column):
                            self.liste_bouttons[row][column].on_left_click()
    
    def exit(self):
        self.root.quit()

    def is_clicked(self, i, j):
        return self.liste_bouttons[i][j].clicked

    def is_flagged(self, i, j):
        return self.liste_bouttons[i][j].state == ButtonState.FLAGGED
