import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+', '-']

print("Welcome to the password generator!")

nr_letters = int(input("How many letters would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

nr_char_total = nr_letters + nr_numbers + nr_symbols

raw_user_pass = []
final_user_pass = []
pass_letter = []
pass_number = []
pass_symbol = []

#First we'll generate 3 lists of random letters, numbers and symbols (Partially random)
for i in range(0, nr_letters):
    int_random = random.randint(0, len(letters) - 1)
    pass_letter.append(letters[int_random])

for i in range(0, nr_numbers):
    int_random = random.randint(0, len(numbers) - 1)
    pass_letter.append(numbers[int_random])

for i in range(0, nr_symbols):
    int_random = random.randint(0, len(symbols) - 1)
    pass_letter.append(symbols[int_random])

raw_user_pass = pass_letter + pass_number + pass_symbol

#Now we will shuffle the combined list in order to randomize the indices (Fully random)
for i in range(0, nr_char_total):
    int_random = random.randint(0, len(raw_user_pass) - 1)
    final_user_pass.append(raw_user_pass[int_random])
    raw_user_pass.pop(int_random)

#Transforming into a string
str_dummy = ""
final_user_pass = str_dummy.join(final_user_pass)

print(f"Here is your password: {final_user_pass}")



