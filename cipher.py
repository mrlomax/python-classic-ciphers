from enum import Enum, auto
from typing import Union
import string

class Cipher(Enum):
    CAESAR = auto()
    VIGENERE = auto()

def _transform_character(char: str, offset: int, direction: int) -> str:
    """Transforms a single character using the provided offset and direction
    Args:
        char (str): The character to be transformed
        offset (int): How much to shift the alphabet
        direction (int): 1 for right shift, -1 for left shift. Right shift by default.

    Returns:
        str: The resulting encrypted/decrypted char.
    """
    alphabet = string.ascii_lowercase
    if not char.isalpha():
        return char

    is_upper = char.isupper()
    index = alphabet.find(char.lower())
    new_index = (index + offset * direction) % len(alphabet)
    new_char = alphabet[new_index]
    
    return new_char.upper() if is_upper else new_char

#Caesar Cipher
def caesar(message: str, offset: int, direction: int = 1) -> str:
    """Encrypts or Decrypts a message using a Caesar cipher with provided offset
    Args:
        message (str): The message to be transformed
        offset (int): How much to shift the alphabet
        direction (int): 1 for right shift, -1 for left shift. Right shift by default. 

    Returns:
        str: The resulting encrypted/decrypted message.
    """
    final_message = []

    for char in message:
        new_char = _transform_character(char, offset, direction)
        final_message.append(new_char)
    return "".join(final_message)

#Vigenere Cipher
def vigenere(message: str, key: str, direction: int=1) -> str:
    """Encrypts or Decrypts a message using a Vigenere cipher with provided offset and key
    Args:
        message (str): The message to be transformed
        key (str): Vigenere cipher key
        direction (int): 1 for right shift, -1 for left shift. Right shift by default. 

    Returns:
        str: The resulting encrypted/decrypted message.
    """
    key_index = 0
    alphabet = string.ascii_lowercase
    final_message = []

    for char in message:
        # Offset calculation
        if char.isalpha():
            key_char = key[key_index % len(key)]
            offset = alphabet.index(key_char)
            key_index += 1
        else:
            offset = 0 # No offset for non-letters
        
        transformed_char = _transform_character(char, offset, direction)
        final_message.append(transformed_char)
    return "".join(final_message)

def encrypt(message: str, key: Union[str, int], cipher_type: Cipher) -> str:
    """Encrypts using provided cipher type
    Args:
        message (str): The message to be encrypted
        key (str or int): Vigenere cipher key or Caesar cipher alphabet offset
        cipher_type (Cipher): Which type of cipher to use

    Returns:
        str: The encrypted message
    """    
    if cipher_type == Cipher.VIGENERE:
        # Check if the key is a string for Vigenere
        if not isinstance(key, str):
            raise TypeError('Vigenere cipher requires a string key')
        return vigenere(message, key)
    
    if cipher_type == Cipher.CAESAR:
        # Check if the key is an int for Caesar
        if not isinstance(key, int):
            raise TypeError('Caesar cipher requires an int key')
        return caesar(message, key)   

def decrypt(message: str, key: Union[str, int], cipher_type: Cipher) -> str:
    """Decrypts using provided cipher type
    Args:
        message (str): The message to be decrypted
        key (str or int): Vigenere cipher key or Caesar cipher alphabet offset
        cipher_type (Cipher): Which type of cipher to use

    Returns:
        str: The decrypted message
    """       
    if cipher_type == Cipher.VIGENERE:
        # Check if the key is a string for Vigenere
        if not isinstance(key, str):
            raise TypeError('Vigenere cipher requires a string key')
        return vigenere(message, key, -1)
    
    if cipher_type == Cipher.CAESAR:
        # Check if the key is an int for Caesar
        if not isinstance(key, int):
            raise TypeError('Caesar cipher requires an int key')
        return caesar(message, key, -1)   

def main():
    text = 'Hello, World! This is a test.'
    shift = 3
    custom_key = 'python'

    caesar_encryption = encrypt(text, shift, Cipher.CAESAR)
    caesar_decryption = decrypt(caesar_encryption, shift, Cipher.CAESAR)

    vigenere_encryption = encrypt(text, custom_key, Cipher.VIGENERE)
    vigenere_decryption = decrypt(vigenere_encryption, custom_key, Cipher.VIGENERE)

    print(f'Offset: {shift}')
    print(f'\nKey: {custom_key}')
    print(f'\nOriginal text: {text}')
    print(f'\nCaesar encrypted text: {caesar_encryption}')
    print(f'\nCaesar decrypted text: {caesar_decryption}')
    print(f'\nVigenere encrypted text: {vigenere_encryption}')
    print(f'\nVigenere decrypted text: {vigenere_decryption}\n')

if __name__ == '__main__':
    main()