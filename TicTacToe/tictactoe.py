import random
from SpielerMensch import SpielerMensch

class TicTacToe:
    def __init__(self): self.spielfeld = None
    
    def __spielfeld_ausgeben(self):
        print(" " + self.spielfeld[0] + " | " + self.spielfeld[1] + " | " + self.spielfeld[2])
        print("---+---+---")
        print(" " + self.spielfeld[3] + " | " + self.spielfeld[4] + " | " + self.spielfeld[5])
        print("---+---+---")
        print(" " + self.spielfeld[6] + " | " + self.spielfeld[7] + " | " + self.spielfeld[8])
        print("---+---+---")

    def spielen(self, spieler1, spieler2):

        self.spielfeld = [str(i) for i in range(1, 10)]
        self.__spielfeld_ausgeben()
        
        if random.randint(1, 2) == 1:
            spieler = spieler1
            spieler1.symbol = "x"
            spieler2.symbol = "o"
        else: 
            spieler = spieler2
            spieler1.symbol = "o"
            spieler2.symbol = "x"

        spiel_vorbei = False

        while not spiel_vorbei:
            gültiger_zug = False
            while not gültiger_zug:
                feld = spieler.zug(self.spielfeld)
                if feld <= 9 and feld >= 1 and self.spielfeld[feld - 1] != "x" and self.spielfeld[feld - 1] != "o"
            feld = spieler.zug(self.spielfeld)
            self.spielfeld[feld - 1] = spieler.symbol
            
            self.__spielfeld_ausgeben()

            if spieler == spieler1: spieler = spieler2
            else: spieler = spieler1


ttt = TicTacToe()
ttt.spielen(SpielerMensch("Alex"), SpielerMensch("Steve"))