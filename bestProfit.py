"""
the function should return the the best profit I could 
have made from 1 purchase and 1 sale of 1 Apple stock yesterday.


>>> get_max_profit([10, 7, 5, 8, 11, 9])
6

"""


def get_max_profit(daily_prices = [10,7,5,8,11,9]):
  """ Search for the max profit one can obtain """
  if len(daily_prices) < 2:
    raise IndexError('need at least two prices')

  #greedily update max_profit and min_price, so initialize them to the first possible values
  max_profit = daily_prices[1] - daily_prices[0]
  min_price = daily_prices[0]
  for t,price in enumerate(daily_prices):
  
    if t == 0:
      continue
    #check profit at time t if we bought at min_price
    profit_at_t = price - min_price
    #update min price if new min is found
    min_price = min(price, min_price)
    #update max profit if new high profit found
    max_profit = max(profit_at_t, max_profit)

  return max_profit

if __name__ == '__main__':
  import doctest
  doctest.testmod()
