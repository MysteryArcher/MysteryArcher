class SpielerMensch:
    def __init__(self, name: str) -> None:
        self.name =  name
        self.symbol = None
    
    def zug(self, spielfeld: list) -> int:
        gültige_eingabe = False
        while not gültige_eingabe:
            feld_str = input(self.name + ", auf welches Feld möchtest du setzen ? ")
            try:
                feld_int = int(feld_str)
                gültige_eingabe = True
            except:
                if spielfeld[feld_int] == "x" and spielfeld[feld_int] == "o": print("Eingabe nicht gültig. Bitte nochmal !")
                print("Eingabe nicht gültig. Bitte nochmal !")
                
        return feld_int