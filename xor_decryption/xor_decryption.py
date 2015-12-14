import csv
import os
import itertools


def solve_problem():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    ciphertext_file_path = os.path.join(script_directory, 'p059_cipher.txt')
    with open(ciphertext_file_path) as names_file:
        dirty_cipher_text = list(csv.reader(names_file))[0]
    cipher_text = map(int, dirty_cipher_text)
    key, message = find_key(cipher_text, key_set=range(ord('a'), ord('z')), key_length=3,
                            known_plaintext=' the ')
    return sum(message)


def find_key(cipher_text, key_set, key_length, known_plaintext):
    """
    Args:
        cipher_text (list[int]): The encrypted message to which we are trying to find the key. Each
            letter of the message should be an item in the list and should be an ASCII value
            (e.g. 'a' is 97, 'b' is 98 ...)
        key_set (list[int]): Possible characters in the key. Like the cipher_text, each letter is
            an item in the list and the letter is represented by the ASCII code of that letter.
        key_length (int): How long the key is
        known_plaintext (str): If decrypted, the plaintext message should contain this string

    Returns:
        list[int], list[int]: The key and plaintext message, both represented as a list of integers
            where each item in the list is the ASCII value of the letter
    """
    for key in itertools.permutations(key_set, key_length):
        message = decrypt(key, cipher_text)
        if known_plaintext in ''.join(map(chr, message)):
            return key, message
    return None


def decrypt(key, cipher_text):
    """
    Args:
        key (list[int]): ASCII values representing an XOR decryption key
        cipher_text (list[int]): ASCII values representing an XOR encrypted message

    Returns:
        list[int]: ASCII values representing the decrypted message

    >>> decrypt([107, 101, 121], [112, 101, 101, 108, 101])
    [27, 0, 28, 7, 0]
    >>> decrypt([107, 101, 121], [27, 0, 28, 7, 0])
    [112, 101, 101, 108, 101]
    """
    return [x ^ y for x, y in zip(cipher_text, itertools.cycle(key))]
