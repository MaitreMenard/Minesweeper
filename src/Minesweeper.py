import tkinter as tk
import random
from Field import Field
from Case import Case
from Etiquette import Etiquette
from Chrono import Chrono

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
        
        self.cadreMenu = tk.Frame(self.root)
        self.cadreMenu.grid(row=0, column=0)
        self.mb = tk.Menubutton(self.cadreMenu,anchor=tk.W,text="Game")
        self.mb.grid(row=0, column=0)
        self.mb.menu = tk.Menu(self.mb,tearoff=0)
        self.mb["menu"] = self.mb.menu
        self.mb.menu.add_command(command=self.new_game,label="New Game")
        self.mb.menu.add_command(command=self.statistics,label="Statistics")
        self.mb.menu.add_command(command=self.options,label="Options")
        self.mb.menu.add_command(command=self.exit,label="Exit")
        
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
                if self.field[i,j] == 0:
                    lab = Etiquette(self, i, j, 0, " ")
                elif self.field[i,j] == 1:
                    lab = Etiquette(self, i, j, 1, "1")
                elif self.field[i,j] == 2:
                    lab = Etiquette(self, i, j, 2, "2", "forest green")
                elif self.field[i,j] == 3:
                    lab = Etiquette(self, i, j, 3, "3", "orange red")
                elif self.field[i,j] == 4:
                    lab = Etiquette(self, i, j, 4, "4", "navy")
                elif self.field[i,j] == 5:
                    lab = Etiquette(self, i, j, 5, "5", "brown")
                elif self.field[i,j] == 6:
                    lab = Etiquette(self, i, j, 6, "6", "light sea green")
                elif self.field[i,j] == 7:
                    lab = Etiquette(self, i, j, 7, "7", "black")
                elif self.field[i,j] == 8:
                    lab = Etiquette(self, i, j, 8, "8", "gray")
                else:
                    lab = Etiquette(self, i, j, -1, "x", "black")
                    
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
        
    def statistics(self):
        fen_statistics = tk.Tk()
        fen_statistics.title("statistics")
        tableFrame = tk.Frame(fen_statistics, height = 30, width = 30)
        tableFrame.grid(row=1, pady=1)
        tableFrame['relief']=tk.SUNKEN
        tableFrame["borderwidth"]=5
        
        tk.Label(tableFrame, text="Difficulty").grid(row=1,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text="Easy").grid(row=1,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="Medium").grid(row=1,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="Hard").grid(row=1,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Game Started").grid(row=2,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(self.nbrGames)).grid(row=2,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=2,column=3,padx=5,pady=5)
        tk.Label(tableFrame, text="N/A").grid(row=2,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Game Won").grid(row=3,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(self.nbrWins)).grid(row=3,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=3,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=3,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="% Game Won").grid(row=4,column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(int(100*self.nbrWins/self.nbrGames))+"%").grid(row=4,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=4,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=4,column=4,padx=5,pady=2)
        tk.Label(tableFrame, text="Best Time").grid(row=5, column=1,padx=5,pady=2)
        tk.Label(tableFrame, text=str(self.highScore)).grid(row=5,column=2,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=5,column=3,padx=5,pady=2)
        tk.Label(tableFrame, text="N/A").grid(row=5,column=4,padx=5,pady=2)

        close = tk.Button(fen_statistics, command=fen_statistics.destroy, text="close")
        close.grid(row=2, padx=100, pady=25)
    
    def options(self):
        fen_options = tk.Tk()
        fen_options.title("options")
        close = tk.Button(fen_options, command=fen_options.destroy, text="close")
        close.grid(padx=100, pady=50)
    
    def exit(self):
        self.root.quit()