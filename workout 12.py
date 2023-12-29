# most repeating characters 

from collections import Counter
from operator import itemgetter


words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_word(words):
    max_rep_count = 0
    output = ''
    for word in words:
        rep_count = max(Counter(word).values())
        if rep_count > max_rep_count:
            max_rep_count = rep_count
            output = word
    
    return output

op = most_repeating_word(words)
print(op)


