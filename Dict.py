from collections import OrderedDict

from collections import deque

quotes = OrderedDict([('Moe', 'A wise guy, huh?'),('Larry', 'Ow!'),('Curly', 'Nyuk nyuk!'),])
for stooge in quotes:
    print(stooge)


def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

print palindrome('a')

print palindrome('racecar')

print palindrome('halibut')
