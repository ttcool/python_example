import array
import binascii

s = 'This is the array.'
a = array.array('c',s)

print 'As string:',s
print 'As array:',a
print 'As hex:',binascii.hexlify(a)

import pprint

a = array.array('i',xrange(3))
print 'Initial:',a

a.extend(xrange(3))
print 'Extended:',a

print 'Slice:',a[2:5]

print 'Iterator:'
print list(enumerate(a))

