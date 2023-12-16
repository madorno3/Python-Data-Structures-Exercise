
from collections import Counter
def vowel_count(phrase):
    vowels = "aeiouAEIOU"
    string = phrase.lower()
    count = Counter(string)
    vowel_counts = {vowel: count[vowel] for vowel in vowels}
    return vowel_counts
    