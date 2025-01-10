import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
dic_of_phonetic_alphabets = {word.letter: word.code for (letter, word) in df.iterrows()}
user_input = input("Enter a word: ").upper()
code_word = [dic_of_phonetic_alphabets[letter] for letter in user_input]
print(code_word)