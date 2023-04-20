"""This was a nice starting easy challenge to get warmed up. For the next time I will improve more my notes and guides. Today I learned that Pandas and list comprehension are your best friends.
"""

# import pandas as pd

# df = pd.read_csv('morse_code_alphabet.csv')

# morse_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# I've built the morse code dictionary using the above code from a comma separated CSV file

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

is_going = 'YES'
while is_going == 'YES' or is_going == 'Y':
    user_input = input("What string do you want to convert? ").upper()

    for letter in user_input:
        print(f"{letter}:   {morse_dict[letter]} \n")

    is_going = input(
        "Would you like to convert another String? Type 'Y' or 'Yes' or anything else to quit ").upper()
