#wersja jako atrybut funkcji
def licznik4() -> int:
    #jeśli atrybut istnieje to defaultowo ma wartośc 0, jeśli istnieje to wartośc zostanie zwiększona o 1
    licznik4.licznik_stanu = getattr(licznik4, 'licznik_stanu', 0) + 1
    return licznik4.licznik_stanu

# for _ in range(10):
#     print(licznik4()) 