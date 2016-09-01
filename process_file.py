import string
import random

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line = line.replace('-','')
   
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
     
        hist[word] = hist.get(word,0) + 1


def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key,value in hist.items():
        t.append((value,key))
    t.sort(reverse=True)
    return t

def print_most_common(hist,num=20):
    t = most_common(hist)
    print 'The most common words are:'
    for freq,word in t[:num]:
        print word,'\t',freq


def random_word(hist):
    t = []
    for word,freq in hist.items():
        t.extend([word] * freq)
    return random.choice(t)



hist = process_file('52934-0.txt')

print hist
print total_words(hist)

print different_words(hist)


print_most_common(hist)

print_most_common(hist,5)

print random_word(hist)
