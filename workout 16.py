# dictdiff


d1 = {'a':1, 'b':2, 'd':3}
d2 = {'a':1, 'b':2, 'c':4}

def dictdiff(d1,d2):
    all_keys = d1.keys() | d2.keys()

    difference = {}

    for key in all_keys:
        d1_value = d1.get(key)
        d2_value = d2.get(key)
        if d1_value != d2_value:
            difference[key] = [d1_value,d2_value]
    
    return difference


result = dictdiff(d1,d2)
print(result)
