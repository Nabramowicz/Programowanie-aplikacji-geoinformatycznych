import time

#2

#funkcja do nadania jednostki czasu
def timer(unit='microseconds'):
    #właściwa funkcja do dekoracji
    def decor(fun):
        #funkcja, w której mierzy sie czas
        def wrap(*args, **kwargs):
            #pomiar czasu
            start_time = time.time()
            result = fun(*args, **kwargs) #zwracam to co dekorowana funkcja zwraca
            end_time = time.time()
            execution_time = end_time - start_time

            #wyświetlenie wyników, bądź ValueError przy błędnej jednostce
            if unit == 'microseconds':
                print(f"-------------------------------------------------------------\n"
                    f"{fun.__name__} execution time: {execution_time} microseconds\n"
                    f"-------------------------------------------------------------\n")
            elif unit == 'seconds':
                execution_time_s = execution_time / 1e6
                print(f"-------------------------------------------------------------\n"
                    f"{fun.__name__} execution time: {execution_time_s} seconds\n"
                    f"-------------------------------------------------------------\n")
            else:
                raise ValueError("Invalid unit. Choose 'seconds' or 'microseconds'.")

            return result
        return wrap
    return decor


#test
@timer(unit='microseconds')
def countdown(n):
    num = n 
    while n > 0:
        n -= 1
    print(f"Countdown to {num} completed")

countdown(5) 
countdown(5000000) 