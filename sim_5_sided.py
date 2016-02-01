def rand5():
  """Write a function that uses rand7 to get a random number between 1 and 5"""
  roll = rand7()
  return roll if roll <=5 else rand5()
