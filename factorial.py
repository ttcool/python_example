def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n* recurse
        return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(4)
print "\n"
print fibonacci(5)

print factorial(3)
print "\n"
print factorial(4)
