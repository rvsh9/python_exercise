# content info in a file 

def wordcount(file_name):
    with open(file_name) as f:
        char_count = 0
        line_count = 0
        all_words = []
        for line in f:
            line_count+=1
            words = line.strip().split()
            all_words = all_words + words
            char_count+= len(line)
        print(all_words)
        print(f'line count = {line_count} \nchar count = {char_count} \ntotal words = {len(all_words)} \nuniqe words = {len(set(all_words))}')

wordcount('./helper files/wcfile.txt')
