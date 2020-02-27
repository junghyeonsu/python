def plus(a,b):
    return int(a)+int(b)

def minus(a,b):
    return int(a)-int(b)

def multiple(a,b):
    return int(a)*int(b)

def divide(a,b):
    if b == 0:
        return None
    else:
        return int(a)/int(b)

a = 10
b = "2"

result = plus(a,b)
print(result)