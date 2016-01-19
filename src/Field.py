import random

class Field:
    def __init__(self, heigh, width, mines):
        self.field = []
        for i in  range(heigh):
            ligne = []
            for j in range(width):
                ligne.append(0)
            self.field.append(ligne)
        while mines > 0:
            mineX = random.randrange(width)
            mineY = random.randrange(heigh)
            if self.field[mineY][mineX] != "x":
                self.field[mineY][mineX] = "x"
            else:
                continue
            mines -= 1
        for i in range(heigh):
            for j in range(width):
                if self.field[i][j] != "x":
                    if i-1 >= 0 and j-1 >= 0 and self.field[i-1][j-1] == "x":
                        self.field[i][j] += 1
                    if i-1 >= 0 and self.field[i-1][j] == "x":
                        self.field[i][j] += 1
                    if i-1 >= 0 and j+1 < width and self.field[i-1][j+1] == "x":
                        self.field[i][j] += 1
                    if j-1 >= 0 and self.field[i][j-1] == "x":
                        self.field[i][j] += 1
                    if j+1 < width and self.field[i][j+1] == "x":
                        self.field[i][j] += 1
                    if i+1 < heigh and j-1 >= 0 and self.field[i+1][j-1] == "x":
                        self.field[i][j] += 1
                    if i+1 < heigh and self.field[i+1][j] == "x":
                        self.field[i][j] += 1
                    if i+1 < heigh and j+1 < width and self.field[i+1][j+1] == "x":
                        self.field[i][j] += 1
    
    def getValue(self, i, j):
        return self.field[i][j]
    
    def setValue(self, i, j, value):
        self.field[i][j] = value
        
    def __getitem__(self, index):
        i,j = index
        return self.field[i][j]
    
    def __setitem__(self, index, value):
        i,j = index
        self.field[i][j] = value
        
    def __str__(self):
        """
        Methode qui convertit le field en une chaine de caracteres.
        """
        string = ""
        for i in range(len(self.field)):
            string = string + str(self.field[i]) + "\n"
        return string


if __name__ == "__main__":
    WIDTH = 9
    HEIGHT = 9
    nbrMines = 10 
    field = Field(HEIGHT, WIDTH, nbrMines)
    print(field)