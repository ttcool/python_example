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

for letter in 'abcde':
    print '%s : %d' % (letter,c[letter])

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory,foo='bar')
print 'd:',d
print 'foo =>',d['foo']

d = collections.deque('abcdefg')
print 'Deque:',d
print 'Length:',len(d)
print 'Left end:',d[0]
print 'Right end',d[-1]

d.remove('c')
print 'remove(c):',d

d1 = collections.deque()
d1.extend('abcdefg')
print 'extend:',d1
d1.append('h')
print 'append:',d1

d2 = collections.deque()
d2.extendleft(xrange(6))
print 'extendleft:',d2
d2.appendleft(6)
print 'appendleft:',d2

print 'From the right:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.pop(),
    except IndexError:
        break
print

print '\nFrom the left:'
d = collections.deque(xrange(6))
while True:
    try:
        print d.popleft(),
    except IndexError:
        break
print 

import threading
import time

candle = collections.deque(xrange(5))

def burn(direction,nextSource):
    while True:
        try:
            next = nextSource()
        except  IndexError:
            break
        else:
            print '%8s: %s' % (direction,next)
            time.sleep(0.1)
    print '%8s done' % direction
    return

left = threading.Thread(target=burn,args=('Left',candle.popleft))
right = threading.Thread(target=burn,args=('Right',candle.pop))

left.start()
right.start()

left.join()
right.join()

d = collections.deque(xrange(10))
print 'Normal:',d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Right rotation:',d



d = collections.deque(xrange(10))
d.rotate(-2)
print 'Left rotation:',d
