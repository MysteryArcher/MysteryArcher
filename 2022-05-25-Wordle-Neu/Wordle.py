import tkinter
from random import choice
from tkinter import *
from tkinter import messagebox
import webbrowser

from Wordlist import wörterbuch

class Wordle:
    def __init__(self):
        self.version = "v1.0"
        self.wörterbuch = wörterbuch
        self.wort = None
        self.grün = "#009900"
        self.gelb = "#ffd633"
        self.grau = "#666666"
        self.schwarz = "#000000"
        self.weiß = "#ffffff"
        self.wurzel = None
        self.abschickenButton = None
        self.versuch = 0

    # Setzt das Attribut wort auf ein zufälliges Wort aus dem Wörterbuch
    def wort_auswählen(self) -> None:
        self.wort = choice(self.wörterbuch)

    # Erhält ein Eingabewort und gibt dessen Auswertung als Liste von fünf Farben zurück
    def auswerten(self, eingabewort: str) -> list:
        antwort = ["grau", "grau", "grau", "grau", "grau"]

        wort_kopie = self.wort
        for i in range(len(eingabewort)):
            if eingabewort[i] == wort_kopie[i]:
                antwort[i] = "grün"
                wort_kopie = wort_kopie[:i] + "_" + wort_kopie[i + 1:]

        for i in range(len(eingabewort)):
            for j in range(len(wort_kopie)):
                if eingabewort[i] == wort_kopie[j] and antwort[i] != "grün":
                    antwort[i] = "gelb"
                    wort_kopie = wort_kopie[:j] + "_" + wort_kopie[j + 1:]
                    break

        return antwort

    def spielerwahl(self):
        eingegebenes_wort = self.eingabe.get().upper()
        self.versuch += 1
        auswertung = self.auswerten(eingegebenes_wort)
        for j in range(len(eingegebenes_wort)):
            label = Label(self.wurzel, text=eingegebenes_wort[j], font="Minecraft")
            label.grid(row=self.versuch, column=j, padx=10, pady=10)
            if auswertung[j] == "grün":
                label.config(bg=self.grün, fg=self.schwarz)
            elif auswertung[j] == "gelb":
                label.config(bg=self.gelb, fg=self.schwarz)
            else:
                label.config(bg=self.grau, fg=self.weiß)

        label.update()

        if auswertung == ["grün", "grün", "grün", "grün", "grün"]:
            messagebox.showinfo(message="Glückwunsch, du hast das Wort gefunden!")
        elif self.versuch == 6:
            messagebox.showwarning(message="Spiel vorbei! Das richtige Wort wäre " + str(self.wort) + " gewesen.")
            self.abschickenButton["state"] = "disabled"
            self.wurzel.destroy()

    def stop(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit ?", icon="warning"): self.wurzel.destroy()

    def show_credits(self):
        webbrowser.open_new_tab("https://www.farning.de")
        messagebox.showinfo("About...", "Dieses Wordle wurde von der Farning-Programmierschule geschrieben.")

    def about_wordle(self): webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Wordle")

    def spielen(self):
        self.wort_auswählen()

        self.wurzel = Tk()
        self.wurzel.title("Wordle")
        self.wurzel.iconbitmap("icon.ico")
        self.wurzel.protocol("WM_DELETE_WINDOW", self.stop)
        self.wurzel.config(bg=self.schwarz)

        self.image = PhotoImage(file="icon.png")
        self.icon = Label(self.wurzel, image=self.image)

        self.versuch = 0

        self.eingabe = Entry(self.wurzel)
        self.eingabe.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

        self.abschickenButton = Button(self.wurzel, text="Abschicken", command=self.spielerwahl, font = "Minecraft")
        self.abschickenButton.grid(row=999, column=3, columnspan=2)
        self.quitButton = Button(self.wurzel, text="Schließen", command=self.stop, font="Minecraft", width=12)
        self.quitButton.grid(row=1000, column=1)
        self.creditsButton = Button(self.wurzel, text="Über uns", command=self.show_credits, font="Minecraft", width=9)
        self.creditsButton.grid(row=1000, column=3)
        self.aboutWordle = Button(self.wurzel, text="Was ist Wordle ?", command=self.about_wordle, font="Minecraft", width=12)
        self.aboutWordle.grid(row=1001, column=1)
        self.versionLabel = Label(self.wurzel, text=self.version, font="Minecraft", fg="#ffffff", bg="#000000")
        self.versionLabel.grid(row=1001, column=3)

        self.wurzel.mainloop()
            


# GEHEN vs WIEGE

w = Wordle()
# w.wort = "GEHEN"
# print(w.auswerten("WIEGE"))
w.spielen()

# TODO Für die Sommerferien: Die GUI optisch verbessern