#1

class ReservationError(Exception):
    def __init__(self, message = "There was a problem with the seat reservation :/"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
    
