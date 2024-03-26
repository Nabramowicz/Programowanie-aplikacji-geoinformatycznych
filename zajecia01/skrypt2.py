import json
import math
import random
import re
import numpy as np

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
print(potega)

tekst = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1,2,3,4,5])
print(losowa)

#Łańcuchy znaków
tekst = f"Wartość: {tekst}"
print(tekst)

print(len(tekst))

print(tekst[1:4])

print(dir(tekst))

tekst = tekst.upper()
print(tekst)

# tekst[1] = 'p'

#LISTY
lista = list(tekst)
print(lista)
lista = lista[:8]
print(lista)
lista.append([1,2,3,4,5])
print(lista)
lista.remove(":")
print(lista)

lista2 = [1,2,3,"banan", 100]
#2 sposoby
#wyrażenie listowe
lista3 = [lista2[x]**2 for x in range(len(lista2)) if lista2[x] != 'banan']
#pętla for z if
lista3 = []
for i in range(len(lista2)):
    if lista2[i] != "banan":
        lista3.append(lista2[i]**2)
    else:
        continue

print(lista3)

lista4 = [*range(2,16,2)]
print(lista4)


#SŁOWNIKI
ja = {}
ja['imie'] = 'Natalia'
ja['nazwisko'] = 'Abramowicz'
ja['wiek'] = 22
ja['rodzice'] = [{'imie': 'Izabela', 'wiek':46},
                 {'imie': 'Krzysztof', 'wiek':51}]

print(ja)
print(ja['rodzice'])
print(ja['rodzice'][0]['imie'])
print(ja.keys())
print(any(ja.keys()) == 'rodzenstwo') 


#KROTKI
krotka = (1,2,"3",4,2,5)
print(len(krotka))
print(krotka.count(2))
#krotka[0] = 2
# print(krotka)

#ZBIORY
X = set('kalarepa')
#X = {'kalarepa'} => tak wejdzie całe słowo 
Y = set('lepy') 
#teraz wychodzą pojedyncza literki, 
#ale jak da się w podwójny nawias to wejdzie całe słowo do zbioru
#Y = set(('lepy')) => {'lepy'}

#część wspólna
X&Y


#INSTRUKCJE
imie = ['Natalia', 'Aleksander', 'Filip', 'Izabela', 'Krzysztof', 'Emilia', 'Tymon']
for idx, name in enumerate(imie):
    print(f"Indeks: {idx}; Imię: {name}")

liczby = {'a':13, 'b':4, 'c':7.13, 'd':0, 'e':-8, 'f':10}

for key in liczby:
    if (liczby[key] % 2 == 0) & (liczby[key] > 0):
        print(f"Liczba {key}: {liczby[key]} jest dodatnia i parzysta.")
    if (liczby[key] != 0):
        print(f"Liczba {key}: {liczby[key]} jest różna od zera.")

owoce = ["jabłko", "banan", "truskawka", "melon", "borówka", "porzeczka"]

if (input("Podaj nazwę owocu i sprawdź czy jest dostępny: ").lower() in owoce):
    print("Owoc jest dostępny")
else:
    print("Owoc nie jest dostęny")
    
suma = 0
while(suma < 100):
    a = int(input("Podaj liczbę: "))
    suma += a
else:
    print(f"Suma podanych liczb przekroczyła 100. Wynosi teraz {suma}")


#DZIWACTWA
#1
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")    

#2
L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")


#PRACA Z PLIKAMI
with open('weather_data.txt', 'r') as file:
 content = file.read()


#ZADANIA SPRAWDZAJĄCE
with open("cw1/teksty.json", "r") as file:
    cat_lovers = json.load(file)

zadanie = {}

#Zamień wszystkie duże litery na małe,
zadanie['1'] = [{key.lower() : value.lower() for key, value in tekst.items()}
                for tekst in cat_lovers["teksty"]]

#Podziel go na wyrazy - będzie to najprawdopodobniej lista
zadanie['2'] = [{key : value.split() for key, value in tekst.items()} 
                 for tekst in cat_lovers["teksty"]]

#Usuń znaki interpunkcyjne – w tekście występują jedynie kropki i przecinki
zadanie['3'] = [{key: [word.strip(".,") for sentence in value for word in re.findall(r"[\w]+|[^\w\s]", sentence) if word.strip(".,")] 
                for key, value in tekst.items()} 
                for tekst in zadanie['2']]

#Zmodyfikuj tak każdy wyraz, żeby w każdym ostatni znak był w formacie dużej litery np. wyraz KozA
zadanie['4'] = [{key: [word[:-1]+word[-1].upper() for word in value]
                 for key, value in tekst.items()}
                 for tekst in zadanie['2']]

#Z listy usuń wyrazy, które nie posiadają w sobie znaku a lub A - można wykorzystać składnię list składanych
zadanie['5'] = [{key: [word for word in value if 'a' in word or 'A' in word]
                 for key, value in tekst.items()}
                 for tekst in zadanie['2']]

#Stwórz zmienną, które będzie przechowywać wszystkie unikatowe wyrazy - można wykorzystać zbiory
zadanie['6'] = list(set(word for i in zadanie['3'] 
                        for word_list in i.values() 
                        for word in word_list))

#stwórz zmienną, która będzie przetrzymywać ilość wystąpień dla każdego ze słów występujących w tekście - można wykorzystać słowniki
zadanie['7'] = [{key: {word: value.count(word) for word in value} 
                 for key, value in text.items()} 
                 for text in zadanie['3']]







