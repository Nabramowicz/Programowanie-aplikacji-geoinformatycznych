from fleet.station import Ambulance
from operations import IncidentQueue, Incident

class AssignAmbulance():

    def __init__(self, incident_queue):
        self.incident_queue = incident_queue

    #aktualizująca się lista dostępnych karetek
    @property
    def available_ambulance(self):
        return [ambulance for ambulance in Ambulance.ambulance_list() if ambulance.status.lower() == 'available']
    
    def nearest_ambulance(self):
        ambulance_loc = {ambulance.id:ambulance.location for ambulance in self.available_ambulance}
        incident_loc = {incident.id:incident.location for incident in self.incident_queue}
        
        while self.available_ambulance and self.incident_queue:
            nearest_amb = [[((i[0] - a[0])**2 + (i[1] - a[1])**2)**0.5 
                            for a in ambulance_loc.values()] 
                            for i in incident_loc.values()]
            
            if any(nearest_amb):
                min_distance = min(min(distance) for distance in nearest_amb)
                min_distances = [distance for distances in nearest_amb for distance in distances]
                incident_id = list(incident_loc.keys())[min_distances.index(min_distance) // len(ambulance_loc)]
                ambulance_id = list(ambulance_loc.keys())[min_distances.index(min_distance) % len(ambulance_loc)]
                
                print("Incident", incident_id, "Nearest ambulance :", ambulance_id)

                del incident_loc[incident_id]
                del ambulance_loc[ambulance_id]
            else:
                break

        print("Ambulance locations:", ambulance_loc)
        print("Incident location:", incident_loc)



    def __str__(self):
        return "\n".join(str(ambulance) for ambulance in self.available_ambulance)


if __name__ == "__main__":

    ambulance1 = Ambulance(
        vehicle_type="AZ124",
        status="Available",
        location=(50.285340, 19.920282),
        medical_equipment=["defibrillator", "stretcher"]
    )
    
    ambulance3 = Ambulance(
        vehicle_type="AZ2011",
        status="Unavailable",
        location=(50.095340, 19.922482),
        medical_equipment=["defibrillator", "stretcher"]
    )

    # aa = AssignAmbulance()

    ambulance4 = Ambulance(
        vehicle_type="AZ2012",
        status="Available",
        location=(50.095340, 19.922562),
        medical_equipment=["defibrillator", "stretcher"]
    )

    # print(aa)
    # print(" ")

    ambulance5 = Ambulance(
        vehicle_type="AZ2016",
        status="Available",
        location=(50.095340, 19.770282),
        medical_equipment=["defibrillator", "stretcher"]
    )

    # print(aa)

    iq = IncidentQueue()
    incident1 = Incident("Power outage in sector 4", "Low", "9.37 PM", (50.094840, 19.920282), "-", "New")
    incident2 = Incident("Power outage in White House", "High", "9.38 PM", (50.095340, 20.920282), "-", "New")
    incident3 = Incident("Fire alarm in building 21", "High", "1.38 AM", (50.094840, 19.920282), "-", "New")
    incident4 = Incident("Fire alarm in building 22", "High", "1.32 AM", (50.095340, 21.920282), "-", "New")
    iq += incident1
    iq += incident2
    iq += incident3
    iq += incident4

    aa = AssignAmbulance(iq)
    print(aa.nearest_ambulance())
    