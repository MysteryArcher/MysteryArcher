import random

from Wordle import Wordle

class Solver:
    # Erhält eine Wordle-Instanz und versucht diese mittels bloßem Raten von Wörtern zu lösen
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def random_solve(self, wordle: Wordle) -> int:

        anzahl_versuche = 0

        while True:

            anzahl_versuche += 1

            # Zufällg ein Wort aussuchen
            wort = random.choice(wordle.wörterbuch)

            # Diese Kombination im Wordle ausprobieren
            if wordle.auswerten(wort) == ["grün", "grün", "grün", "grün", "grün"]:
                # Falls sie richtig war, beende
                return anzahl_versuche


    # Erhält eine Wordle-Instanz und versucht diese mittels systematischem Ausprobieren von Wörtern zu lösen
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def brute_force_solve(self, wordle: Wordle) -> int:            
        
        for i in range(len(wordle.wörterbuch)):
            if wordle.auswerten(wordle.wörterbuch[i]) == ["grün", "grün", "grün", "grün", "grün"]:
                return i + 1

     # Gibt True zurück, falls wort mit allen bisherigen Ergebnissen noch möglich ist, ansonsten False
    def __wort_konsistent(self, wort: str, bisherige_ergebnisse: dict) -> bool:
        if wort in bisherige_ergebnisse.keys():
            return False
        for eingegebenes_wort, ergebnis in bisherige_ergebnisse.items():
            if not self.__wort_konsistent_mit(wort, eingegebenes_wort, ergebnis):
                return False
        return True

    def __wortfilter(self, wordle: Wordle, bisherige_ergebnisse: dict) -> list:
        mögliche_worter = []
        for wort in wordle.wörterbuch:
             if self.__wort_konsistent(wort, bisherige_ergebnisse):
                mögliche_worter.append(wort)
        return mögliche_worter

    # Gibt True zurück, falls wort mit eingegebenes_wort und ergebnis noch möglich ist, ansonsten False
    def __wort_konsistent_mit(wort: str, eingegebenes_wort: str, ergebnis: list) -> bool:
        # Graue Buchstaben überprüfen
        for i in range(len(eingegebenes_wort)):
            if ergebnis[i] == "grau":
                # Wie oft kommt eingegebenes_wort[i] in eingegebenes_wort grün oder gelb vor
                anzahl = 0
                for j in range(len(eingegebenes_wort)):
                    if eingegebenes_wort[i] == eingegebenes_wort[j] and ergebnis[i] != "grau":
                        anzahl += 1
                for i in range(len(eingegebenes_wort)):
                    if ergebnis[i] != "grau":
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
        # TODO Hausaufgaben für den 9. Juli : gelbe Buchstaben überprüfen korrigieren
        # Gelbe Buchstaben überprüfen
        # for i in range(len(wort)):
        #    if ergebnis[i] == "gelb":
        #        if wort[i] == eingegebenes_wort[i] or not eingegebenes_wort[i] in wort:
        #            return False
        #        else:
        #            # Markiere Buchstaben als bereits verwendet
                    wort = wort[:i] + "_" + wort[i+1:]
        # Graue Buchstaben überprüfen
        buchstabenzähler = {}
        for buchstabe in eingegebenes_wort:
            buchstabenzähler[buchstabe] = 0
            wurde_gegraut = False
            for i in range(len(eingegebenes_wort)):
                if ergebnis[i] != "grau" and eingegebenes_wort[i] == buchstabe and wort[i] != "_":
                    buchstabenzähler[buchstabe] += 1
                if ergebnis[i] == "grau" == eingegebenes_wort[i] == buchstabe:
                    wurde_gegraut = True
                # Bedingung 2
                if wurde_gegraut and buchstabenzähler[buchstabe] != wort.count(buchstabe):
                    return False
        # True wird rausgegeben falls Bedingung 2 nicht falsch wird.                  
        return True 

        for i in range(len(wort)):
            if ergebnis[i] == "grau" and eingegebenes_wort[i] in wort:
                return False
        return True

    # Erhält eine Wordle-Instanz und versucht diese möglichst intelligent zu lösen, d.h. die Anzahl benötigter
    # Versuche soll minimiert werden
    # Falls erfolgreich, wird die Anzahl benötigter Versuche zurückgegeben, ansonsten -1
    def intelligent_solve(self, wordle: Wordle) -> int:
        anzahl_versuche = 0
        ergebnisse = {}
        while True:
            anzahl_versuche += 1
            geratenes_wort = random.choice(self.__wortfilter(ergebnisse, wordle))
            ergebnisse[geratenes_wort] = wordle.auswerten(geratenes_wort)
            if wordle.auswerten(geratenes_wort) == ["grün", "grün", "grün", "grün", "grün"]:
                return anzahl_versuche

w = Wordle()
s = Solver()
w.wort_auswählen()
print(s.random_solve(w))