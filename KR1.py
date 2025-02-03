def decorator(Uskorenie):
    def wrapper(v0,v1,t):
        print(Uskorenie(v0,v1,t))
        print(v0*t+Uskorenie(v0,v1,t)*t**2/2)
    return wrapper

@decorator
def Uskorenie(v0,v1,t):
    a=(v1-v0)/t
    return a

try:
    v0=float(input('Введите начальную скорость'))
    v1=float(input('Введите конечную скорость'))
    t=float(input('Введите время'))
    a=1/t
    Uskorenie(v0,v1,t)
except ValueError:
    print('значения должны быть числами')
except ZeroDivisionError:
    print('Время не может быть 0')
