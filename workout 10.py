# using + operator

def my_sum(*items):
    if not items:
        return items

    output = items[0]
    for element in items[1:]:
        output+=element
    
    return output

x = my_sum(1,2,3)
y = my_sum([1,2],[3,4])
z = my_sum('ab','cd')

print(x)
print(y)
print(z)