import sys
import random
import string


password = []
characters_left = -1

def update_characters_left(number_of_characters):
    """oblicza ile zostalo wolnych znaków"""
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków spoza przedziału: 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)



password_lenght = input("Jak długie ma byc haslo? ")

if password_lenght.isdigit() == False:
    print("Musisz podać cyfry!")
    sys.exit(0)
else:
    password_lenght = int(password_lenght)

if password_lenght < 5:
    print("Hasło jes za krotkie. Hasło musi mieć miniumum 5 znaków.")
    sys.exit(0)
else:
    characters_left = password_lenght


lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane, hasło zostanie uzupełnione małymi literami.")
    lowercase_letters += characters_left

print()
print("Długość hasła:", password_lenght)
print("Małe litery:", lowercase_letters)
print("Duże litery:", uppercase_letters)
print("Znaki specjalne:", special_characters)
print("Cyfry:", digits)

for _ in range(password_lenght):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło:","".join(password))