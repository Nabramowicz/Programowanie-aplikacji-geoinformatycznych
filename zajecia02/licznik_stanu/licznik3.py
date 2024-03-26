#wersja z klasa z atrybutem instancji
class Licznik3:
    #inicjalizacja wartośc licznika stanu na 0
    def __init__(self) -> None:
        self.licznik_stanu = 0

    #__call__ do wywołyania obiektu tak jak funkcji
    def __call__(self) -> int:
        self.licznik_stanu += 1
        return self.licznik_stanu

licznik3 = Licznik3()

for _ in range(10):
    print(licznik3()) 
