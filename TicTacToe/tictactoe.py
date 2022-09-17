class TTT:
    def __init__(self):
        self.SPIELFELD = [str(i) for i in range(1, 10)]
        self.RUNNING = True
        self.player_names = ["", ""]
        for i in range(2):
            self.player_names[i] = input("Player " + str(i + 1) + " name : ")
        self.TURN = self.player_names[0]

    def ask_input_question(self) -> int:
        try:
            self.choice = int(input("Bitte nummer eingeben : "))
        except ValueError:
            print("Antwort nicht gültig. Sie müssen eine Ziffer zwischen 0 und 9 eingeben.")
            self.ask_input_question()
        return self.choice

    def run(self):
        while self.RUNNING:

            print(" " + self.SPIELFELD[0] + " | " + self.SPIELFELD[1] + " | " + self.SPIELFELD[2])
            print(" ---------")
            print(" " + self.SPIELFELD[3] + " | " + self.SPIELFELD[4] + " | " + self.SPIELFELD[5])
            print(" ---------")
            print(" " + self.SPIELFELD[6] + " | " + self.SPIELFELD[7] + " | " + self.SPIELFELD[8])
            print(" ---------")

            print("Spieler " + self.TURN + " am Zug ;")
            self.value = self.ask_input_question()
            if self.TURN == self.player_names[0]:
                self.SPIELFELD[self.value - 1] = "X"
                self.TURN = self.player_names[1]
            elif self.TURN == self.player_names[1]:
                self.TURN = self.player_names[0]
                self.SPIELFELD[self.value - 1] = "O"


if __name__ == "__main__":
    TTT().run()

# TODO Hausaufgaben für den 25.09.22 : Ein funktionsfähiges Tic Tac Toe für zwei menschliche Spieler.