def multiple_letter_count(phrase):
    str_dict = dict()
    for char in phrase:
        if char in str_dict:
            str_dict[char]+=1
        else:
            str_dict[char]=1
    return str_dict
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """