from .ambulance import Ambulance
from personnel.driver import Driver
from personnel.employee import Employee

class Station:
    __max_id = 1

    def __init__(self, location, ambulance, driver, employee):
        self.station_id = Station.__max_id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1

        if self.is_driver_an_employee(self.driver, self.employee):
            raise ValueError("The driver and the employee cannot be the same person!")

    def is_ambulance_at_location(self):
        return self.location == self.ambulance.location
    
    def is_driver_an_employee(self, driver, employee):
        return driver.employee_id == employee.employee_id

if __name__ == "__main__":
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    
    employee1 = Employee("John", "Doe", 12000.0)

    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    station1 = Station((50.095340, 19.920282), ambulance2 , driver2, employee1)
    station3 = Station((50.095340, 19.920281), ambulance2 , driver2, employee1)
    # station2 = Station((50.095340, 19.920282), ambulance2 , driver2, driver2)

    print(f"Is ambulance {ambulance2.id} at location {station1.station_id}:", station1.is_ambulance_at_location())
    print(f"Is ambulance {ambulance2.id} at location {station3.station_id}:", station3.is_ambulance_at_location())
    # print("Is ambulance at location:", station2.is_ambulance_at_location())
