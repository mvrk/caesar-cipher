import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted = ''


def encrypt(message, shift):
    encrypted = ''
    if shift < 0 or shift > 26:
        shift = shift % 26
    for char in message:
        if not char.isalpha():
            encrypted.append(char)
        else:
            index = alphabet.find(char.lower())
            index += shift
            if index >= 26:
                index -= 26
            if index < 0:
                index += 26
            if char.isupper():
                letter = alphabet[index]
                encrypted += letter.upper()
            if char.islower():
                encrypted += alphabet[index]
    return encrypted


def decrypt(encrypted, shift):
    return encrypt(encrypted, -shift)


def crack():
    pass
