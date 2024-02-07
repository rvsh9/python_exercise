a = [3,2,5,2,6,2,5,6,62,61]

def qsort(arr):
    if len(arr) <= 1:
        return arr    
    pivot = arr[0]
    left_arr = [val for val in arr[1:] if val < pivot]
    right_arr = [val for val in arr[1:] if val >= pivot]
    # print(f'pivot = {pivot} \nleft_arr = {left_arr} \nright_arr = {right_arr}')

    return qsort(left_arr) + [pivot] + qsort(right_arr)

x = qsort(a)

print(a)
print(x)
