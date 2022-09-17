import string

# Wörterbuch-liste
from Wordlist import wörterbuch # So wenig wie möglich importieren

letters = list(string.ascii_uppercase) # Etwas schneller und eleganter als händisch alle Buchstaben einzutragen

letters_freq = [0] * len(letters) # Kürzer und kein Hardcoding (jetzt könnte man letters verändern und letters_freq passt sich automatisch an)

max_freq = 0
letter_freq = " "

# Immer gut, alle Variablen aussagekräftig zu benennen
# Dadurch wird der Code besser lesbar, verständlich für andere, und auch das Fehlersuchen leichter
for word in wörterbuch:
    for letter_word in word:
        for i in range(len(letters)): # Kein Hardcoding
            if letter_word == letters[i]:
                letters_freq[i] += 1
                if letters_freq[i] > max_freq:
                    max_freq = letters_freq[i]
                    letter_freq = letters[i]

print("Most frequent letter:", letter_freq, "Frequency:", max_freq)