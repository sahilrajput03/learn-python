# A map object is a generator returned from calling the map() built-in function. It is intended to be iterated over (e.g. by passing it to list()) only once, after which it is consumed. Trying to iterate over it a second time will result in an empty sequence.

def myFunc(n):
  return len(n)

x1 = map(myFunc, ('apple', 'banana', 'cherry'))
print(list(x1)) # << Thats how we convert `tuple` to `list`(i.e., array).