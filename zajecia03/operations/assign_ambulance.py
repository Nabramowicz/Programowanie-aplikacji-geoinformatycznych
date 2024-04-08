from fleet.station import Ambulance
from operations import IncidentQueue, Incident

class AssignAmbulance():
    def __init__(self, incident_queue):
        self.incident_queue = incident_queue
        self.assignment_details = []
        self.assign_ambulance()


    #aktualizująca się lista dostępnych karetek
    @property
    def available_ambulance(self):
        return [ambulance for ambulance in Ambulance.ambulance_list() if ambulance.status.lower() == 'available']


    def display_ambulance_list(self):
        ambulance_list = Ambulance.ambulance_list()
        for ambulance in ambulance_list:
            print(ambulance)


    def update_handled_incident_info(self, incident_id, ambulance_id):
        #zmiana statusu incydentu   
        self.incident_queue(incident_id).status = 'Incident handled'
        #zmiana statusu karetki, która obsługuje dane zdarzenia
        for ambulance_obj in Ambulance.ambulance_list():
            if ambulance_obj.id == ambulance_id:
                ambulance = ambulance_obj
                ambulance.status = 'On mission'
                ambulance.other = f'Handles incident {incident_id}'
                break

        return self
    
    #metoda zwracająca przypisania karetek do incydentów
    def get_assignment_details(self):
        return self.assignment_details
    
    #metoda do przypisywania karetek do zdarzeń
    def assign_ambulance(self):
        #zabranie pod id lokalizacji
        ambulance_loc = {ambulance.id: ambulance.location for ambulance in self.available_ambulance}
        incident_loc = {incident.id: incident.location for incident in self.incident_queue}
        
        while ambulance_loc and incident_loc:
            #pierwszy incydent z listy (wg priorytetu)
            incident_id, i_loc = list(incident_loc.items())[0]
            #euclidean distances
            distances = [(ambulance_id, ((i_loc[0] - a_loc[0])**2 + (i_loc[1] - a_loc[1])**2)**0.5)
                        for ambulance_id, a_loc in ambulance_loc.items()]
            ambulance_id, distance = min(distances, key=lambda x: x[1]) #zwraca id karetki i dystans
                    
            # print("Incident", incident_id, "Nearest available ambulance :", ambulance_id, "distance: ", distance)

            self.update_handled_incident_info(incident_id, ambulance_id)
            self.assignment_details.append((incident_id, ambulance_id, distance))

            del incident_loc[incident_id]
            del ambulance_loc[ambulance_id]

        return self
    

    def __str__(self):
        result = ""
        for assignment in self.assignment_details:
            incident_id, ambulance_id, distance = assignment
            result += f"Incident ID: {incident_id}, Assigned ambulance ID: {ambulance_id}, Distance: {distance}\n"
        return result

    

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

    # # aa = AssignAmbulance()

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
    print(aa)
    print(iq)
    aa.display_ambulance_list()
    print(aa)