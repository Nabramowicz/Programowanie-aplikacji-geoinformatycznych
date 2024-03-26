#wersja ze zmienną global
licznik_stanu = 0

def licznik2() -> int:
    #wskazuje, że chce użyć zmiennej globalnej, a nie inicjować nową zmienną lokalną
    global licznik_stanu
    licznik_stanu += 1
    return licznik_stanu

for _ in range(10):
    print(licznik2()) 