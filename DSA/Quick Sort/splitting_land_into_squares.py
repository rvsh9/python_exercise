# recursion practice

length = 250
width = 100

def split_land_equally(l,b):
    print('executing function')
    longer = max(l,b)
    shorter = min(l,b)
    print(f'longer = {longer} \nshorter = {shorter}')

    if longer == 2*shorter:
        print('if loop executed')
        return shorter
    
    new_l = shorter
    new_b = longer % shorter
    print(new_l)
    print(new_b)
    return split_land_equally(new_l,new_b)

x = split_land_equally(length,width)

print(x)
