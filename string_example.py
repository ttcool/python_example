import string
 
s = 'The quick brown fox jumped over the lazy dog.'

print s
print string.capwords(s)

leet = string.maketrans('abegiloprstz','463611092572')

print s
print s.translate(leet)


