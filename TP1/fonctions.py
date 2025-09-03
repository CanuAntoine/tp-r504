def puissance(a, b):
    if type(a) is not float and type(a) is not int:
        raise TypeError("Only float and int are allowed")
    if type(b) is not float and type(b) is not int:
        raise TypeError("Only float and int are allowed")
    
    if a == 0 and b < 0:
        raise ValueError("0 cannot be raised to a negative power")
    
    return a ** b
