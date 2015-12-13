# iterator
x = [1, 2, 3]
y = iter(x)
assert 1 in x
print type(y)
print next(y)
print list(y)
print dir(y)
