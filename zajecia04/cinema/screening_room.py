import numpy as np
from exceptions import ReservationError
import string

#1

class ScreeningRoom:
    def __init__(self, rows, cols):
        #siedzenia w sali kinowej to macierz, gdzie miejsca wolne będą zaznaczone jako O a zajęte jako X
        #domyślnie cała sala jest wolna 
        self.seats = np.full((rows, cols), 'O')
        self.rows = rows
        self.cols = cols
        #zarezerwowane miejsca będa przechowywane w słowniku, gdzie kluczem będzie siedzenie
        self.reserved_seats = {}

    #metoda do zamiany nazw miejsc na współrzędne
    def seat_coord(self, seat):
        row = string.ascii_lowercase.find(seat[0].lower()) + 1
        col = int(seat[1:])
        # print(row, col)

        return row, col


    #metoda do rezerwacji miejsc 
    def reserve_seat(self, seat, user):

        row, col = self.seat_coord(seat)

        #ValueError jeśli użytkownik będzie chciał dokonać rezerwacji nieistniejącego miejsca 
        if not (1 <= row <= self.rows) or not (1 <= col <= self.cols):
            raise ValueError('Invalid seat number!')
        
        #zgłoszenie wyjątku o braku dostępnych miejsc
        if  np.all(self.seats == 'X'):
            raise ReservationError("No available seats!")
        
        #zgłoszenie wyjątku o próbie zarezerwowania juz zarezerwowanego miejsca
        if self.seats[row - 1][col - 1] == 'X':
            raise ReservationError("This seat has already been booked!")
        
        #zgłoszenie wyjątku o obecności użytkownika w systemie
        if user in self.reserved_seats.values():
            raise ReservationError("User has already booked a seat!")
    
        
        #jeśli wszystko jest ok, to robi sie rezerwacja miejsca i użytkownik zostaje dodany 
        self.seats[row - 1][col - 1] = 'X'
        self.reserved_seats[seat] = (user)

        return self
    
    
    #usuwanie rezerwacji
    def cancel_reservation(self, seat, user):
        if seat in self.reserved_seats and self.reserved_seats[seat] == user:
            row, col = self.seat_coord(seat)
            self.seats[row - 1][col - 1] = 'O'
            del self.reserved_seats[seat]
        else:
            raise ReservationError("It is not possible to cancel a reservation. Wrong data!")
    

    def __str__(self):
        col_numbers = "   " + " ".join(str(col_no) for col_no in range(1, self.cols + 1))
        seats_str = ''
        for row_idx, row in enumerate(self.seats):
            row_letter = string.ascii_uppercase[row_idx]  #Literka do wierszy
            row_seats = row 
            seats_str += row_letter + '  ' + ' '.join(row_seats) + '\n'
        return col_numbers + '\n' + seats_str


if __name__ == "__main__":

    salaA = ScreeningRoom(5, 10)
    print(salaA)

    salaA.reserve_seat('A2', "Tom Jerry")
    salaA.reserve_seat('E5', "Jerry Tom")
    salaA.reserve_seat('E6', "Anonim")
    salaA.reserve_seat('C9', "Anna Anna")
    print(salaA)

    salaA.cancel_reservation('E5', "Jerry Tom")
    print(salaA)


    #nieistniejące miejsce
    # salaA.reserve_seat('N3', "Tom Jerry")

    #zajęte miejsce
    # salaA.reserve_seat('A2', "Anna Anna")

    #istniejący użtkownik
    salaA.reserve_seat('D3', "Tom Jerry")

    #zły cancel
    # salaA.cancel_reservation('E7', "Jerry Tom")


