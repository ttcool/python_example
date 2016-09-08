import collections

print collections.Counter(['a','b','c','d','b'])
print collections.Counter({'a':2,'c':5,'d':8,'b':9})
print collections.Counter(a=2,b=3,c=1)

c = collections.Counter()
print 'Initial:',c

c.update('abcdaab')
print 'Sequence:',c

c.update({'a':1,'d':5})
print 'Dict:',c
