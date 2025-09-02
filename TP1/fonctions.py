def puissance(a, b):
  if type(a) is not int or type(b) is not int:
    raise TypeError("Only intergers are allowed")

  if a == 0 and b < 0:
    raise ValueError("Value is undefined")
  return a**b
