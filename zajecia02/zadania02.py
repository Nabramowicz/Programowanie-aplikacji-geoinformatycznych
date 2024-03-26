import this
from typing import Any 

#PRZYPISANIA
#6
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(f"Dane - rok: {rok}, język: {jezyk}, wersja: {wersja}")

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(f"Oceny - pierwsza: {pierwsza}, środkowe: {srodek}, ostatnia: {ostatnia}")

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod = info
print(f"Info - imię: {imie}, nazwisko: {nazwisko}, zawód: {zawod}")

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, lista = dane
jezyk, wersja, opis = lista
print(f"Dane - rok: {rok}, jezyk: {jezyk}, wersja: {wersja}, opis: {opis}")

#PRZYPISANIA Z WIELOMA CELAMI I WSPÓŁDZIELONE REFERENCJE
#10
a = b = [1,2,3]
b[0] = "zmieniono"
print(f"b[0] = {b[0]}")
print(a, b)
#Pierwszy wyraz zarówno z liście b, jak i a został zmieniony. 
#Obydwie zmienne wskazują na ten sam obiekt, więc w momencie 
#kiedy wartość obiektu została zmieniona, to wartośc wszyskich zmiennych
#odwołujących się do do niego zostanie także zmieniona.
#Listy są obiektami mutowalnymi tzn., że po stworzeniu można modyfikować ich zawartość.

#11
c = a[:]
c[0] = "nowa wartość"
print(a,b,c)
#Tworząc kopię tworzy się nowy obiekt, więc po zmianie wartości w liście c
#ani a ani b nie uległy zmianie. A i b wskazują na inny obiekt niż c.

#12
x = y = 10
y += 1
print(x, y)
#Po pierwszym przypisaniu x i y wskazywały na ten sam obiekt, 
#ale po inkrementacji y to już inny nowy obiekt (można to sprawdzić funkcją id())
#Wynika z faktu, że integery nie są obiektami mutowalnymi.
#Zatem modyfikacja y nie wpływa na wartość x.


#PRZYPISANIA ROZSZERZONE I WSPÓŁDZIELONE REFERENCJE
#13
K = [1, 2]
L = K #L referencją do tego samego obiektu listy co K
K = K + [3, 4] #przez konkatenację powstała nowa lista [1,2,3,4] i K wskazuje na nowy obiekt, inny niż L.
#Czyli teraz L i K wskazują na inne obiekty, więc będą zwracać inne wartości.
M = [1, 2]
N = M #N referencją do tego samego obiektu listy co M
M += [3, 4] #operator '+=' modyfikuje zmienną stojącą po lewej stronie (M) dodając wartośc po prawej stornie ([3,4])
#Czyli lista M została rozszerzona o kolejne elementy, ale nie powstał nowy obiekt (tak jak w przypadku konkatenacji), 
#więc M i N nadal zwracają taki sam wynik.

print(K,L,M,N)


#TECHNIKI TWORZENIA PĘTLI - uzupełnienie
#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

for z in zip(imiona, oceny):
    print(z)

#Jeśli listy będą miały różne długości to zip() będzie parował 
#elementy tylko do wspólnego maksymalnego indeksu

#15
liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x**2

print(list(map(kwadrat, liczby)))


#ITERATORY
#DOKUMENTOWANIE KODU
#FUNKCJE

#ARGUMENTY
#16
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

a = [1,2,3]
b = 1

print(f"Wynik funkcji zmien_wartosc z argumentem a = {a}: {zmien_wartosc(a)}") #pierwszy element w liście się zmienił
print(f"Wynik funkcji zmien_wartosc z argumentem b = {b}: {zmien_wartosc(b)}") #liczba 'pozornie' się zmieniła
#W przypadku listy zwracany jest ten samo obiekt:
print(id(a) == id(zmien_wartosc(a)))
#W przypadku int zostaje zwrócony nowy obiekt:
print(id(b) == id(zmien_wartosc(b)))

#17
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    pass
    podsumowanie = f"Zamówiono: {nazwa_produktu}, Cena: {cena*ilosc} zł, Ilość: {ilosc} szt."
    return podsumowanie

#a,b
zamowienia = []

for produkt, dane in {"Łóżko":[1200,1], "Fotel":[800,2], "Lampa":[600,3]}.items():
    raport = zamowienie_produktu(produkt, cena=dane[0], ilosc=dane[1])
    zamowienia.append(raport)

for i in zamowienia:
    print(i)

#c, d, e
def zamowienie_produktu2(nazwa_produktu, *, cena, ilosc=1):
    pass
    podsumowanie = f"Zamówiono: {nazwa_produktu}, Cena za sztukę: {cena} zł, Ilość: {ilosc} szt."
    suma = f"Koszt zamówienia: {cena*ilosc} zł."
    raport = (podsumowanie, suma)
    return raport

zamowienia2 = []

for produkt, dane in {"Łóżko":1200, "Fotel":800, "Lampa":600}.items():
    raport= zamowienie_produktu2(produkt, cena=dane)
    zamowienia2.append(raport)

for i in zamowienia2:
    print(i)


#18
def stworz_raport(*args, **kwargs):
    for prod_id in args:
        raport = f"ID produktu: {prod_id} "
        nazwa = kwargs.get(f'nazwa_{prod_id}', '')
        cena = kwargs.get(f'cena_{prod_id}', '')
        raport += f"| Nazwa: {nazwa} | Cena: {cena}"
        print(raport)

stworz_raport(101, 102, nazwa_101="Kubek termiczny", cena_101="45.99 zł", nazwa_102="Długopis", cena_102="4.99 zł")


#ZASIĘGI

#Funkcje fabrykujące - obiekty funkcji, które pamiętają wartości w otaczających zasięgach
#19
def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
         return podstawa**wykladnik
    return poteguj


print(f"Wynik 4^2: {stworz_funkcje_potegujaca(2)(4)}")
#albo
potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(4)) # Wynik: 16

############################################
#20 + 21 przeniesione zgodnie z zdaniem 24
############################################

#FUNKCJE ANONIMOWE LAMBDA
    
#22
ksiazki = [
    {"tytul": "Harry Potter i Więzień Azkabanu", "autor": "J.K. Rowling", "rok_wydania": 1999},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1997},
    {"tytul": "Harry Potter i Zakon Feniksa", "autor": "J.K. Rowling", "rok_wydania": 2003},
    {"tytul": "Harry Potter i Czara Ognia", "autor": "J.K. Rowling", "rok_wydania": 2000},
    {"tytul": "Harry Potter i Insygnia Śmierci", "autor": "J.K. Rowling", "rok_wydania": 2007},
    {"tytul": "Harry Potter i Książę Półkrwi", "autor": "J.K. Rowling", "rok_wydania": 2005},
    {"tytul": "Harry Potter i Komnata Tajemnic", "autor": "J.K. Rowling", "rok_wydania": 1998}
]

#a - sortowanie po roku
sorted(ksiazki, key= lambda d: d['rok_wydania'])

#b - książki wydane tylko po 2000
publ_after_2000 = list(filter(lambda d: d['rok_wydania'] > 2000, ksiazki))

#c - lista tytułów
ksiazki = list(map(lambda d: d['tytul'], ksiazki))
ksiazki


#GENERATORY

#23
def dni_tygodnia():
    yield 'Poniedziałek'
    yield 'Wtorek'
    yield 'Środa'
    yield 'Czwartek'
    yield 'Piątek'
    yield 'Sobota'
    yield 'Niedziela'

#drugie rozwiązanie:
# def dni_tygodnia():
#     days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
#     for day in days:
#         yield day

for day in dni_tygodnia():  
    print(day)

days = dni_tygodnia()
pon_wt_sr = [next(days) for _ in range(3)]
pon_wt_sr


#PAKIETY MODUŁÓW

#24



