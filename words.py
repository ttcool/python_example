
def print_word(file_name,n):
    fin = open(file_name)
    for line in fin:
        word = line.strip()
        if len(word) > n:
            print word

f = 'words.txt'
print_word(f,20)

