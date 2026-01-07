# NATO Alphabet Project
import pandas as pd

data = pd.read_csv("./day 26/nato_phonetic_alphabets.csv")
# print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(alphabets_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)