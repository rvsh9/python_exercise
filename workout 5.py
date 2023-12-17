#pig latin

def to_pig_latin(input_word):
    
    if input_word[0] in 'aeiou':
        return input_word+'way'
    else:
        return input_word[1:]+input_word[0]+'ay'
    

output_word = to_pig_latin('ello')
print(output_word)