import math
import numpy
a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c= int(input('Введите значение c: '))
d = int(input('Введите значение d: '))
a=b/a  
b=c/a 
c=d/a

Q=(a**2-3*b)/9 
R=(2*a**3-9*a*b+27*c)/54 

S=Q**3-R**2 

if S>0:  
    fi=(1/3) * math.acos(R/math.sqrt(Q**3))
    x1=-2 * math.sqrt(Q) * math.cos(fi)-a/3
    x2=-2 * math.sqrt(Q) * math.cos(fi-2*math.pi/3)-a/3
    x3=-2 * math.sqrt(Q) * math.cos(fi+2*math.pi/3)-a/3
    print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
elif S<0: 
    if Q>0:
        fi=(1/3)*math.acosh(math.fabs(R)/math.sqrt(Q**3))
        x1=-2*numpy.sign(R)*math.sqrt(Q)*math.cosh(fi)-a/3
        x2=numpy.sign(R)*math.sqrt(Q)*math.cosh(fi)-a/3-1j*(math.sqrt(3)*math.sqrt(Q)*math.sinh(fi))
        x3=numpy.sign(R)*math.sqrt(Q)*math.cosh(fi)-a/3+1j*(math.sqrt(3)*math.sqrt(Q)*math.sinh(fi))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
    elif Q<0:
        fi=(1/3)*math.asinh(math.fabs(R)/math.sqrt(math.fabs(Q)**3))
        x1 = -2 * numpy.sign(R) * math.sqrt(math.fabs(Q)) * math.sinh(fi) - a / 3
        x2=numpy.sign(R) * math.sqrt(math.fabs(Q)) * math.sinh(fi) - a / 3 + 1j * (math.sqrt(3) * math.sqrt(math.fabs(Q)) * math.cosh(fi))
        x3=numpy.sign(R) * math.sqrt(math.fabs(Q)) * math.sinh(fi) - a / 3 - 1j * (math.sqrt(3) * math.sqrt(math.fabs(Q)) * math.cosh(fi))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')
    else: 
        x1 = -(c - (a ** 3) / 27) ** (1 / 3) - a / 3
        x2=(-a+x1)/2+1j*((1/2)*math.sqrt(math.fabs((a-3 * x1) * (a + x1) - 4 *b)))
        x3=(-a+x1)/2-1j*((1/2)*math.sqrt(math.fabs((a-3 * x1) * (a + x1) - 4*b)))
        print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}, x3 = {(numpy.round(x3, 2))}')

else: 
    x1=-2*R**1/3-a/3 
    x2=x3=R**1/3-a/3
    print(f'x1 = {(numpy.round(x1, 2))}, x2 = {(numpy.round(x2, 2))}')