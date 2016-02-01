"""
Write a function get_products_of_all_ints_except_at_index() 
that takes a list of integers and returns a list of the products.

>>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
[84, 12, 28, 21]
"""

def get_products_of_all_ints_except_at_index(input_list):

  #calculate the product of all ints before index

  prods_except = [None]*len(input_list)
  prod = 1

  i = 0
  while i < len(input_list):
    prods_except[i] = prod
    prod *= input_list[i]
    i+=1

  #now get the product of all integers after that int, since each
  #index already has the product of all ints before it, we're just storing the total
  #product of all other integers
  prod = 1
  i = len(input_list) - 1
  
  while i >=0:
    prods_except[i] *= prod
    prod *= input_list[i]
    i -= 1

  return prods_except


if __name__ == '__main__':
  import doctest
  doctest.testmod()
