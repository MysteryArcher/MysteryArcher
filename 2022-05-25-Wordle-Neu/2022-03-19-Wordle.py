import random
from colored import stylize, fg

from Wordlist import wörterbuch



# wort = random.choice(wörterbuch)
# print(wort)

# print(wort[0])

# eingabe = input("Welches Wort möchtest du eingeben? ").upper()


# gefärbter_string = stylize("Ich bin rot!", fg(1))
# print(gefärbter_string)

farbe1 = 10

#ausgabe = stylize(eingabe[0], fg(farbe1)) + 

#TODO 02.04.2022 weiterarbeiten/optimieren
#TODO Solver/Grafik

#TODO Alle Lösungen auf GitHub laden

# dictionary = { "weiß": 1, "schwarz": 2 }
# print(dictionary["weiß"]) # 1
# print(dictionary["schwarz"]) # 2
# dictionary["weiß"] = 2
# dictionary = dict()

def wortfilter(bisherige_ergebnisse: dict) -> list:
    mögliche_worter = []
    for wort in wörterbuch:
        if wort_konsistent(wort, bisherige_ergebnisse):
            mögliche_worter.append(wort)
    return mögliche_worter

# Gibt True zurück, falls wort mit allen bisherigen Ergebnissen noch möglich ist, ansonsten False
def wort_konsistent(wort: str, bisherige_ergebnisse: dict) -> bool:
    if wort in bisherige_ergebnisse.keys():
        return False
    for eingegebenes_wort, ergebnis in bisherige_ergebnisse.items():
        if not wort_konsistent_mit(wort, eingegebenes_wort, ergebnis):
            return False
    return True
#TODO Hausaufgabe auf 28. Mai: diese beiden Funktionen

# Gibt True zurück, falls wort mit eingegebenes_wort und ergebnis noch möglich ist, ansonsten False
def wort_konsistent_mit(wort: str, eingegebenes_wort: str, ergebnis: list) -> bool:
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
                wort = wort[:i] + "_" + wort[i+1:]
    # Graue Buchstaben überprüfen
    for i in range(len(wort)):
        if ergebnis[i] == "grau" and eingegebenes_wort[i] in wort:
            return False
    return True
print(wort_konsistent_mit("BAUER", "SAUER", ["grau", "grün", "grün", "grün", "grün"]))
print(wort_konsistent_mit("BIRNE", "INSEL", ["gelb", "gelb", "grau", "gelb", "grau"]))
print(wort_konsistent_mit("FEIND", "LIEGE", ["grau", "gelb", "gelb", "grau", "gelb"]))




d = { "HALLO": ["grün", "gelb", "grau", "grau", "gelb"], "BAUER": ["grau", "gelb", "grün", "grau", "grau"] }

# TODO Hausaufgabe auf 21. Mai
# 1. Recherchiere die Funktion ord()
# 2. Erstelle ein Dictionary, in dem für jeden Kleinbuchstaben sein ASCII-Wert (Position in der ASCII-Tabelle) gespeichert ist

# buchstaben = dict()
# for i in range(97, 123):
#     buchstaben[chr(i)] = i
# print(buchstaben)

# TODO Am 21. Mai wort_konsistent_mit zusammen