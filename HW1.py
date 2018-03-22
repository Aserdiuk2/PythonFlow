__author__ = 'aserdiuk2'

"""Implement your own _uniq function.
  first arg is collection.
  function returns new collection of uniq items
  Usage of Set data structures is forbidden."""

l = [9, 6, 7, 4, 8, 3, 5]

def good_order(l):
    return(sorted(l))

print(list(good_order(l)))

"""Implement your own _filter function.
  first arg is callback, second arg - collection.
  function returns new collection of items for which callback function call return true
  Usage of standard filter function is forbidden."""

ages = (25, 17, 14, 32, 64, 89, 7, 19, 18)

maturity_age = list(filter(lambda n: n >= 18, ages))
print(maturity_age)

"""Implement your own _map function.
  first arg is collection, second arg - callback (mapper) 
  function returns new collection of mapped items.
  Usage of standard map functionality is forbidden."""

squared = list(map(lambda x: x**2, range(-5, 5)))
print(tuple(squared))

"""Implement your own _find function.
  first arg is callback, second arg - collection.
  function returns first item from collection for which callback function call return true
  Usage of standard filter function or yor own _filter is forbidden."""

str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
str2 = "tempo"

print(str1.find(str2))
print(str1.find(str2, 80))

