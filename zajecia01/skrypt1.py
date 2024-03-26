#4,5
print("Hello World")
help(print)


#Moduły i przestrzenie nazw
print("Moduły i przestrzenie nazw\n")
#1
from os import getcwd
from importlib import reload

current_path= getcwd()
print(current_path)


import czas
print(f"\n{czas.aktualny_czas}")

import time 
time.sleep(20)
print(czas.aktualny_czas)

reload(czas)

print(czas.aktualny_czas)

#Podstawowe typy wbudowane

