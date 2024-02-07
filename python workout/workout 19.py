# password to dict

def passwd_to_dict(file_name):
    final_dict = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                words = line.split(':')
                final_dict[words[0]] = words[2]
    
    return final_dict

result = passwd_to_dict('./helper files/passwd.txt')

print(result)
for name,id in enumerate(result):
    print(f'{name},{id}\n')