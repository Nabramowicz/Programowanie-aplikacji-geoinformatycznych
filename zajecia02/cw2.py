import sys
print(sys.path)

lista1 = [1,2,3,4]
lista2 = ["abc",'a', 'b']

for z in zip(lista1,lista2):
    print(z) 
# 4 obetnie bo nie ma z czym sparować

def fun1(x):
    """
    Args:
    x(int): podaj liczbę
    """
    return x**2

for z in map(fun1,lista2):
    print(z)

#argumenty vchce mieć takiego typu,, na wyjściu str
def fun2(x: int, y: str) -> str:
    x = x + y
    return x

print(fun2(1,2))

#obiekty mutowalne i niemutowalne
a = [1,2,3,4]
b = 12

def fun3(x,y):
    x[0] = "123"
    y = 56789
    return x

#a[:] jest tak zrobie to utworzę kopię i w efekcie wyjdzie inny wu=ynik - zmienna a nie zostanie zmieniaona
print(fun3(a,b))


def fun4(*args, **kwargs):
    print(args)
    print(kwargs)

#args gromadzi argumenty bez nazwy, a kwargs przyjmuje argumenty, które mają zdefiniowaną nazwę
fun4(1,2,3,4,5, b="123", c="kotek_psotek")

#zasięg lokalny (np. zmienna w funkcji)
#zasięg globalny (np.zmienna zdefiniowana poza funkcją)
#LEGB - Local, Enclosing, Global (deklarowane na poziomie całego modułu, definiowane poprzez global), Built-in 
#nonlocal 

#funkcje mają być niezależne od otoczenia
#bez zmiennych globalnych
#funkcja ma miec jeden cel, ma być możliwie mała

#atrybuty i adnotacje
#print(dir(...))

#FUNKCJE ANONIMOWE
x = lambda y: y**2
print(x(6))

#GENERATORY
def fun5(a):
    for i in a:
        yield i**2
    
generator  = fun5([1,2,3])
type(generator)
for i in generator:
    print(i)

#ZADANIA

