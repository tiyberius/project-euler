import string
import os
import csv


def solve_problem():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    names_file_path = os.path.join(script_directory, 'p022_names.txt')
    with open(names_file_path) as names_file:
        names = list(csv.reader(names_file))[0]
    return calculate_names_scores(sorted(names))


def calculate_names_scores(names):
    """
    Args:
        names (list): A list of names for which we are calculating a "name score" as describe in
            https://projecteuler.net/problem=22

    Returns:
        int: The cumulative score for all names

    Examples:
        >>> calculate_names_scores(["MARY","PATRICIA","LINDA"])
        331
    """
    names_score = 0
    for index, name in enumerate(names, start=1):
        alphabetical_value = get_alphabetical_value_for_name(name)
        names_score += alphabetical_value * index
    return names_score


def get_alphabetical_value_for_name(name):
    """
    Args:
        name (str): The name for which we want to calculate the alphabetical value

    Returns:
        int: The alphabetical value for the given name

    Examples:
        >>> get_alphabetical_value_for_name('colin')
        53
        >>> get_alphabetical_value_for_name('kyle')
        53
        >>> get_alphabetical_value_for_name('BOB')
        19
    """
    alphabetical_value = 0
    for letter in name:
        alphabetical_value += get_alphabetical_position(letter)
    return alphabetical_value


def get_alphabetical_position(letter):
    """
    Args:
        letter (str): The letter you need the alphabetical position for

    Returns:
        int: The position in the alphabet for the given letter

    Examples:
        >>> get_alphabetical_position('a')
        1
        >>> get_alphabetical_position('o')
        15
        >>> get_alphabetical_position('T')
        20
        >>> get_alphabetical_position('z')
        26
        >>> get_alphabetical_position('$')
        0
    """
    # http://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
    try:
        return string.lowercase.index(letter.lower()) + 1
    except ValueError:
        return 0
