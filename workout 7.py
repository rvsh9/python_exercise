# ubbi dubbi word 

def ubbi_dubbi(word):
       
    output = []

    for alphabet in word:
        if alphabet in 'aeiou':
            output.append('ub' + alphabet)
        else:
            output.append(alphabet)
    
    return ''.join(output)

print(ubbi_dubbi('octopus'))
