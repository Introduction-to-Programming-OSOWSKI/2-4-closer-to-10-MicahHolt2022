#WRITE YOUR CODE IN THIS FILE
def close10(a,b):
    if abs((10 - a)) > abs((10 - b)):
        return b
    elif abs((10 - b)) > abs((10 - a)):
        return a
    else:
        return 0

print(close10(5,15))
