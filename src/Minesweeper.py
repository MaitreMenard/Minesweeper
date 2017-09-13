import tkinter as tk
import random
from field import Field
from Case import Case
from Etiquette import Etiquette
from Chrono import Chrono
from view.menu import Menu
from view.options_window import OptionsWindow
from view.statistics_window import StatisticsWindow

class Minesweeper():
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.nbrMines = mines
        self.minesLeft = mines
        self.chrono = None
        self.liste_bouttons = []
        self.root = tk.Tk()
        self.root.title('Minesweeper')
        
        self.menu = Menu(self.root, self.new_game, self.on_statistics_window_opened,
                          self.on_options_window_opened, self.exit)

        self.smiley = tk.PhotoImage(file="smiley.gif").subsample(2, 2)
        
        self.cadre1 = tk.Frame(self.root, height = 48, width = 250)
        self.cadre1.grid(row = 1, padx = 10, pady = 1)
        self.cadre1.grid_propagate(0)
        self.cadre1['relief']=tk.SUNKEN
        self.cadre1["borderwidth"]=5
        self.frame1 = tk.Frame(self.cadre1, height = 21, width = 80)
        self.frame1.grid(row=0,column=0)
        self.frame1.grid_propagate(0)
        self.frameSmiley = tk.Frame(self.cadre1)
        self.frameSmiley.grid(row=0,column=3)
        self.frameTime = tk.Frame(self.cadre1)
        self.frameTime.grid(row=0,column=5)
        self.label_MinesLeft = tk.Label(self.frame1)
        self.label_MinesLeft.grid(padx=10)
        self.label_Time = tk.Label(self.frameTime)
        self.label_Time.grid(padx=30)
        self.smileyButton = tk.Button(self.frameSmiley,image=self.smiley, command=self.new_game, height=32, width=32)
        self.smileyButton.grid(padx=22)
        
        self.cadre2 = tk.Frame(self.root, height = 347, width = 277)
        self.cadre2.grid(padx=6,pady=4)
        self.cadre2['relief']=tk.SUNKEN
        self.cadre2["borderwidth"]=5
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
        self.nbrBouttons = self.width*self.height
        self.updateLabel_MinesLeft()
        if len(self.liste_bouttons) != 0:
            for i in range(self.height):
                for j in range(self.width):
                    self.liste_bouttons[i][j].destroy()
            self.liste_bouttons.clear()
        self.field = Field(self.height, self.width, self.nbrMines)
        labelHeight = 6
        labelWidth = 8
        for i in range(self.height):
            liste_ligne = []
            for j in range(self.width):
                if self.field[i,j] == "x":
                    lab = Etiquette(self, i, j, -1)
                else:
                    lab = Etiquette(self, i, j, self.field[i,j])
                    
                lab.grid(row=i,column=j,padx=labelWidth,pady=labelHeight)
                
                bt = Case(self, i, j, "    ")
                bt.grid(row=i, column=j)
                bt["relief"] = tk.RAISED
                bt["borderwidth"]=3
                bt.grid_propagate(0)
                #bt.config(height = 30)
                liste_ligne.append(bt)
            self.liste_bouttons.append(liste_ligne)
        self.label_Time["text"] = "0"
        if self.chrono == None:
            self.chrono = Chrono()
        else:
            self.chrono.reset()
        self.root.after(1,self.updateLabel_Time)
    
    def updateLabel_MinesLeft(self):
        self.label_MinesLeft['text'] = "Mines : {}".format(str(self.minesLeft))
    
    def updateLabel_Time(self):
        if self.vivant == True:
            if self.started == True:
                if self.win == False:
                    self.label_Time["text"] = "{}".format(str(int(self.chrono.get())))
                    self.root.after(1,self.updateLabel_Time)
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
                self.root.after(1,self.updateLabel_Time)
        
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
    
    def exit(self):
        self.root.quit()
