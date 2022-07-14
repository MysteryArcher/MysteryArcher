from Wordlist import*

letters_freq = []

letters = ["A", "B",  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in range(26):
    letters_freq.append(0)

max_freq = 0
letter_freq = " "

for i in wörterbuch:
    for j in i:
        for k in range(26):
            if j == letters[k]:
                letters_freq[k] += 1
                if letters_freq[k] > max_freq:
                    max_freq = letters_freq[k]
                    letter_freq = letters[k]

print("Most recurrent letter : ", letter_freq, max_freq)
