#wersja ze zmienną nonlocal
def licznik1() -> callable:
    licznik_stanu = 0
    def dodaj() -> int:
        #wskazuje, że zmienna znajduje się w zakresie funkcji zewnętrznej (licznik()) i to ją chcę inkrementować
        nonlocal licznik_stanu
        licznik_stanu += 1
        return licznik_stanu
    return dodaj

l1 = licznik1()
for _ in range(10):
    print(l1()) 