#!/usr/local/bin/python -t

def collatz(x):
    length = 0
    print x,
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x + 1
        print x,
        length += 1

    return length

start = 59
length = collatz(start)
print "\ncollatz(%d) has %d items" % (start, length)

