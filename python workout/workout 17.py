# how_many_different_numbers

numbers = [1, 2, 3, 1, 2, 3, 4, 1]

def how_many_different_numbers(collection):
    return len(set(numbers))


result = how_many_different_numbers(numbers)

print(result)
