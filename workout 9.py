# first last element

def first_last(iterable):
    return iterable[:1]+iterable[-1:]

x = first_last([1,2,3,4])
y = first_last('abc')
z = first_last((1,2,3,4,5))

print(x)
print(y)
print(z)