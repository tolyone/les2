import math as mat

print('input number a=', end='')
a = int(input())

print('Input nubmer b=', end='')
b = int(input())

print (a,b)

def foo(a,b):
    print(a,'+',b,'=',a+b)
    print(a,'-',b,'=',a-b)
    print(a,'/',b,'=',a/b)
    print(a,'*',b,'=',a*b)
    print(a,'**',b,'=',a**b)
    print('sqrt','(',a,')','=',mat.sqrt(a))
    print('sqrt', '(', b, ')', '=', mat.sqrt(b))

foo(a,b)

# принимает любое число, внутри функции корень, умножение, деление