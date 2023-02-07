def myZip(l, m):
    assert len(l) == len(m)
    i = 0
    while i < len(l):
        yield (l[i], m[i])
        i += 1

l = [1, 2]
m = [10, 20]


print( sum( a * b for a, b in  myZip(l, m) ) )


