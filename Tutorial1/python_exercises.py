"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x % 2 == 0:
        return False
    else:
        return True


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    reverse = word[::-1]
    if reverse == word:
        return True
    else:
        return False

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    return [n for n in numlist if n % 2 != 0]

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    result = {}
    tokens = text.lower().split()
    for word in tokens:
        result[word] = result.get(word,0) + 1
    return result