import math

def math_ex(a):
    b = math.sqrt(a)
    print('Square root: ', b)
    c = math.log(a)
    print('Logarithm: ', c)
    d = math.sin(a)
    print('Sine: ', d)

n = int(input('Enter a number: '))
math_ex(n)