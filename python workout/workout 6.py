# pig latin sentence

def p1_sentence(sentence):
    
    words = sentence.split(' ')

    pig_latin_words = []

    for word in words:
        if word[0] in 'aeiou':
            new_word = word + 'way'
        else:
            new_word = word[1:] + word[0] + 'ay'
        
        pig_latin_words.append(new_word)
    
    return " ".join(pig_latin_words)

print(p1_sentence("This is a sample sentence"))
        
        