# read the final line of the file 

def get_final_line(filename):
    with open(filename) as f:
        for line in f:
            pass
        return line
    
result = get_final_line('./helper files/fakelogs.txt')

print(result)