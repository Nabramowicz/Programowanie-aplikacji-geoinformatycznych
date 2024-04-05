from fleet.station import Ambulance

class AssignAmbulance():

    def __init__(self):
        pass

    #aktualizująca się lista dostępnych karetek
    @property
    def available_ambulance(self):
        return [ambulance for ambulance in Ambulance.ambulance_list() if ambulance.status.lower() == 'available']

    def __str__(self):
            return "\n".join(str(ambulance) for ambulance in self.available_ambulance)


if __name__ == "__main__":

    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )    
    ambulance3 = Ambulance(
        vehicle_type="AZ2011",
        status="Unavailable",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    aa = AssignAmbulance()

    ambulance4 = Ambulance(
        vehicle_type="AZ2012",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    print(aa)
    print(" ")

    ambulance5 = Ambulance(
        vehicle_type="AZ2016",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    print(aa)