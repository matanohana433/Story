# caesar cipher
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        is_num = char.isnumeric()
        if char == " ":
            end_text += " "
        elif is_num == True:
            end_text += char
        elif char not in alphabet:
            end_text += '•'
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        if shift % 2 == 0:
            shift = shift / 2
        else:
            shift = shift - 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    keep_playing = input(
        "Want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if keep_playing == "yes":
        game_on = True
    elif keep_playing == "no":
        game_on = False
        print("Game over, bye")
