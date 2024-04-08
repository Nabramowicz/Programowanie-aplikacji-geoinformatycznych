# from operations import *
class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment', 'other']
    __instances_count = 0
    __max_id = 1 #1
    __ambulance_list = []

    def __init__(self, vehicle_type, status, location, medical_equipment, *other):
        self.id = Ambulance.__max_id #1
        self.vehicle_type = vehicle_type
        self.status = status  # e.g., "available", "on_mission", "servicing"
        self.location = location # as (northing, easting)
        self.medical_equipment = medical_equipment  # List of medical equipment names
        self.other = other if other else None
        Ambulance.__instances_count += 1
        Ambulance.__max_id += 1 #1
        Ambulance.__ambulance_list.append(self)

    def update_location(self, new_location):
        self.location = new_location

    def change_status(self, new_status):
        self.status = new_status

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type
    
    def __str__(self):
        other_info = self.other if self.other else "-"
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}, "
                f"Other: {other_info}")
    
    @staticmethod
    def validate_id(ambulance_id):
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__instances_count}"
    
    @classmethod
    def ambulance_list(cls):
        # return [ambulance.status for ambulance in cls.__ambulance_list]
        # return [str(ambulance) for ambulance in cls.__ambulance_list]
        return cls.__ambulance_list
    
    #metoda do ładnego wyświetlania listy karetek
    def ambulance_list_pretty_version():
        pretty_version = [str(ambulance) for ambulance in Ambulance.ambulance_list()]
        return print('\n'.join(pretty_version))



if __name__ == "__main__":
    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )    
    ambulance3 = Ambulance(
        vehicle_type="AZ2011",
        status="Unavailable",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())

    print(Ambulance.ambulance_list())
    ambulance1.change_status("Unavailable")
    print(Ambulance.ambulance_list())
