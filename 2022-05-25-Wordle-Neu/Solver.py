import random
import string
import tkinter as tk
from Wordle import Wordle

class Solver:

    def __init__(self, wordle: Wordle):
        self.wordle = wordle
        self.buchstabenwertungen = {}
        for buchstabe in string.ascii_uppercase:
            self.buchstabenwertungen[buchstabe] = 0
        for wort in self.wordle.wörterbuch:
            for buchstabe in set(wort):
                self.buchstabenwertungen[buchstabe] += 1

        # for key, value in self.buchstabenwertungen.items():
        #     if value > 100:
        #         print(key, value)

        self.wortwertungen = {}
        for wort in self.wordle.wörterbuch:
            wort_wertung = 0
            for buchstabe in set(wort):
                wort_wertung += self.buchstabenwertungen[buchstabe]
            self.wortwertungen[wort] = wort_wertung

        # for key, value in self.wortwertungen.items():
        #     if value > 2300:
        #         print(key, value)


    # Erhält eine Wordle-Instanz und versucht diese mittels bloßem Raten von Wörtern zu lösen
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def random_solve(self) -> int:

        anzahl_versuche = 0

        while True:

            anzahl_versuche += 1

            # Zufällg ein Wort aussuchen
            wort = random.choice(self.wordle.wörterbuch)

            # Diese Kombination im Wordle ausprobieren
            if self.wordle.auswerten(wort) == ["grün", "grün", "grün", "grün", "grün"]:
                # Falls sie richtig war, beende
                return anzahl_versuche


    # Erhält eine Wordle-Instanz und versucht diese mittels systematischem Ausprobieren von Wörtern zu lösen
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def brute_force_solve(self) -> int:
        for i in range(len(self.wordle.wörterbuch)):
            if self.wordle.auswerten(self.wordle.wörterbuch[i]) == ["grün", "grün", "grün", "grün", "grün"]:
                return i + 1

     # Gibt True zurück, falls wort mit allen bisherigen Ergebnissen noch möglich ist, ansonsten False
    def __wort_konsistent(self, wort: str, bisherige_ergebnisse: dict) -> bool:
        if wort in bisherige_ergebnisse.keys():
            return False
        for eingegebenes_wort, ergebnis in bisherige_ergebnisse.items():
            if not self.__wort_konsistent_mit(wort, eingegebenes_wort, ergebnis):
                return False
        return True

    def __wortfilter(self, bisherige_ergebnisse: dict) -> list:
        mögliche_worter = []
        for wort in self.wordle.wörterbuch:
            if self.__wort_konsistent(wort, bisherige_ergebnisse):
                mögliche_worter.append(wort)
        return mögliche_worter

    # Gibt True zurück, falls wort mit eingegebenes_wort und ergebnis noch möglich ist, ansonsten False
    def __wort_konsistent_mit(self, wort: str, eingegebenes_wort: str, ergebnis: list) -> bool:
        # Graue Buchstaben überprüfen
        for i in range(len(eingegebenes_wort)):
            if ergebnis[i] == "grau":
                # Wie oft kommt eingegebenes_wort[i] in eingegebenes_wort grün oder gelb vor
                anzahl = 0
                for j in range(len(eingegebenes_wort)):
                    if eingegebenes_wort[i] == eingegebenes_wort[j] and ergebnis[j] != "grau":
                        anzahl += 1
                if anzahl != wort.count(eingegebenes_wort[i]):
                    return False

        # Grüne Buchstaben überprüfen
        for i in range(len(wort)):
            if ergebnis[i] == "grün":
                if wort[i] != eingegebenes_wort[i]:
                    return False
                else:
                    # Markiere Buchstaben als bereits verwendet
                    wort = wort[:i] + "_" + wort[i+1:]

        # Gelbe Buchstaben überprüfen
        for i in range(len(wort)):
            if ergebnis[i] == "gelb":
                if wort[i] == eingegebenes_wort[i] or not eingegebenes_wort[i] in wort:
                    return False
                else:
                    # Markiere Buchstaben als bereits verwendet
                    index_des_buchstabens_in_wort = wort.find(eingegebenes_wort[i]) # In wort, nicht in eingegebenes_wort!
                    wort = wort[:index_des_buchstabens_in_wort] + "_" + wort[index_des_buchstabens_in_wort+1:]
        
        return True

    def wortwahl(self, ergebnisse) -> str:
        verbleibende_wörter = self.__wortfilter(ergebnisse)
        bestes_wort = verbleibende_wörter[0]
        for wort in verbleibende_wörter:
            if self.wortwertungen[wort] > self.wortwertungen[bestes_wort]:
                bestes_wort = wort
        return wort

    # Erhält eine Wordle-Instanz und versucht diese möglichst intelligent zu lösen, d.h. die Anzahl benötigter
    # Versuche soll minimiert werden
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def intelligent_solve(self) -> int:
        anzahl_versuche = 0
        ergebnisse = {}
        while True:
            anzahl_versuche += 1
            geratenes_wort = self.wortwahl(ergebnisse)
            #print(geratenes_wort)
            ergebnisse[geratenes_wort] = self.wordle.auswerten(geratenes_wort)
            #print(ergebnisse[geratenes_wort])
            if ergebnisse[geratenes_wort] == ["grün", "grün", "grün", "grün", "grün"]:
                return anzahl_versuche

w = Wordle()
s = Solver(w)

# gelöste_instanzen = 0
# for i in range(1000):
#     w.wort_auswählen()
#     if s.intelligent_solve() <= 6:
#         gelöste_instanzen += 1
# print(gelöste_instanzen / 1000)

print(s.wortwahl({"KRIEG": ["grau", "grau", "grau", "grau", "grau"], "DATUM": ["grau", "grau", "grau", "gelb", "grau"], "BUSCH": ["grau", "grün", "gelb", "gelb", "gelb"], "FUCHS": ["grau", "grün", "grün", "grün", "grün"], "WUCHS": ["grau", "grün", "grün", "grün", "grün"]}))

# 1. Was ist der häufigste Buchstabe im Wörterbuch aus Wordlist.py?
# 2. (Optional) Erstelle ein Ranking aller Buchstaben nach Häufigkeit im Wörterbuch aus Wordlist.py! Am besten als Dictionary.

# TODO GUI
