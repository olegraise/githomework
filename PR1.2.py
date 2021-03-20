import math
#Метод хорд

def f(x):
    return ((x-5)**2-math.sin(x-5))
def f1(x):
    return (math.sin(x-5)+2)

a = 4.85
b = 5.2
e = 0.00000000001

if (f(a) * f1(a) > 0):
    c = a
else:
    c = b
if (f(a) * f1(a) < 0):
    x = a
else:
    x = b

while True:
        x1 = f(x) * (x - c) / (f(x) - f(c))
        x = x - x1
        if (math.fabs(x1) < e):
            break;

print("На отрезке оси абсцисс от 4.85 до 5.2 график f(x) пересекает её в точке х =",x)






