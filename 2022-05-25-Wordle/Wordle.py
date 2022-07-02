from random import choice
from Wordlist import wörterbuch

class Wordle:
    def __init__(self):
        self.wörterbuch = wörterbuch
        self.wort = None

    # Setzt das Attribut wort auf ein zufälliges Wort aus dem Wörterbuch
    def wort_auswählen(self) -> None:
        self.wort = choice(wörterbuch)

    # Erhält ein Eingabewort und gibt dessen Auswertung als Liste von fünf Farben zurück
    def auswerten(self, eingabewort: str) -> list:
        antwort = ["grau", "grau", "grau", "grau", "grau"]

        wort_kopie = self.wort
        for i in range(len(eingabewort)):
            if eingabewort[i] == wort_kopie[i]:
                antwort[i] = "grün"
                wort_kopie = wort_kopie[:i] + "_" + wort_kopie[i + 1:]
                print(wort_kopie)

        for i in range(len(eingabewort)):
            for j in range(len(wort_kopie)):
                if eingabewort[i] == wort_kopie[j] and antwort[i] != "grün":
                    antwort[i] = "gelb"
                    wort_kopie = wort_kopie[:j] + "_" + wort_kopie[j + 1:]

        return antwort

wort = "wagen"

eingabewort = "essen"

a = Wordle()
a.wort = wort
print(a.auswerten(eingabewort))
