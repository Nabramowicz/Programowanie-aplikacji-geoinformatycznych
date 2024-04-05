from fleet.ambulance import Ambulance
from operations import IncidentQueue, Incident
from personnel import *


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance3 = Ambulance(
        vehicle_type="AZ2011",
        status="Unavailable",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
        )
    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie kilku zgłoszeń
    incident1 = Incident("Power outage in sector 4", "Low", "6.15 PM", (50.095340, 19.920282), "Emily Addice", "New")
    incident2 = Incident("Fire alarm in building 21", "High", "1.38 AM", (50.095340, 19.920282), "-", "New")
    incident3 = Incident("Fire alarm in building 22", "High", "1.32 AM", (50.095340, 19.920282), "-", "New")
    incident4 = Incident("Power outage in sector 7", "Low", "1.28 AM", (50.095340, 19.920282), "-", "New")
    incident5 = Incident("Fire alarm in building 21", "High", "1.43 AM", (50.095340, 19.920282), "Tom Jerry, employee of the reported building", "New")
    incident6 = Incident("Fire alarm in building 129", "High", "8.15 AM", (50.095340, 19.920282), "-", "New")
    queue += incident1
    queue += incident2
    queue += incident3
    queue += incident4
    queue += incident5
    queue += incident6

    print(" ")

    # wypisz wszystkie zgłoszenia
    print("AKTUALNE ZGŁOSZENIA: \n")
    # print(new_queue)
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")


if __name__ == "__main__":
    run_application()