from datetime import datetime
class Incident:
    __max_id = 1 #1
    __report_time = datetime.now().strftime('%I:%M %p')
    
    def __init__(self, description, priority, time_of_the_report, notifier_info): #2
        self.id = Incident.__max_id #1
        self.description = description
        self.priority = priority #2
        #podawana jest tylko godzina w zgłoszeniu, więc date przyznaje 'dzisiejszą' (na wypadek gdyby karetka nie została przydzielona w ciągu doby jakimś cudem ;)) i łącze to z godziną, która ze string została przerobiona na obiekt datetime 
        self.time_of_the_report = datetime.combine(datetime.now().date(), datetime.strptime(time_of_the_report.replace('.', ':'), '%I:%M %p').time()) #2
        self.notifier_info = notifier_info #2
        Incident.__max_id += 1 #1


    def __repr__(self):
        return (f"Incident(id={self.id!r}, description={self.description!r}, "
                f"priority={self.priority!r}, time_of_the_report={self.time_of_the_report!r}, " #2
                f"notifier_info={self.notifier_info!r})") #2

    def __str__(self):
        return (f"Incident {self.id}: {self.description}\n"
                f"Priority: {self.priority}\n" #2
                f"Time of the report: {self.time_of_the_report}\n" #2
                f"Notifier information: {self.notifier_info}\n") #2