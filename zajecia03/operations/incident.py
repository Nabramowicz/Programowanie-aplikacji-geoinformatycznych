from datetime import datetime
class Incident:
    __max_id = 1 #1
    # __report_time = datetime.now().strftime('%I:%M %p')
    
    def __init__(self, description, priority, time_of_the_report, location, notifier_info, status): #2
        self.id = Incident.__max_id #1
        self.description = description
        self.priority = priority #2
        #podawana jest tylko godzina w zgłoszeniu, więc date przyznaje 'dzisiejszą' i łącze to z godziną, która ze string została przerobiona na obiekt datetime 
        self.time_of_the_report = datetime.combine(datetime.now().date(), datetime.strptime(time_of_the_report.replace('.', ':'), '%I:%M %p').time()) #2
        self.location = location
        self.notifier_info = notifier_info #2
        self.status = status
        Incident.__max_id += 1 #1


    def __repr__(self):
        return (f"Incident(id={self.id!r}, description={self.description!r}, "
                f"priority={self.priority!r}, time_of_the_report={self.time_of_the_report!r}, " #2
                f"location={self.location!r}, notifier_info={self.notifier_info!r}" #2
                f"status={self.status!r})") 

    def __str__(self):
        return (f"Incident {self.id}: {self.description}\n"
                f"Priority: {self.priority}\n" #2
                f"Time of the report: {self.time_of_the_report}\n" #2
                f"Location: {self.location}\n" 
                f"Notifier information: {self.notifier_info}\n"
                f"Status: {self.status}\n") #2