import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in file.iterrows()}
user_input = input("Enter a word: ").upper()
results = [nato[letter] for letter in user_input]