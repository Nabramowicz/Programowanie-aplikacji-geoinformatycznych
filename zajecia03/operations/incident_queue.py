from datetime import datetime, timedelta
from queue import Full
from .incident import Incident

class IncidentQueue:
    #przechowywanie incydentów
    def __init__(self):
        self.__queue = []

    #dostęp do elementów po pozycji
    def __getitem__(self, position):
        return self.__queue[position]

    #dostęp do elementów po wartości
    def __setitem__(self, position, value):
        self.__queue[position] = value

    #
    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.__queue):
            result = self.__queue[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, incident):
        return incident in self.__queue

    def __repr__(self):
        return f"IncidentQueue({self.__queue!r})"

    def __str__(self):
        if len(self):
            incident_text = []
            for idx, incident in enumerate(self.__queue):
                incident_str = incident.__str__()
                incident_info = "\n".join([' ' * 4 * idx + line for line in incident_str.split("\n")])
                incident_text.append(incident_info)
            return "\n".join(incident_text)
        else:
            return "Empty queue"

    def __add__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue.__queue = self.__queue[:] 
            new__queue += other
            return new__queue.prioritize_reports()
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Incident):
            new__queue = IncidentQueue()
            new__queue += other
            new__queue.__queue += self.__queue
            return new__queue.prioritize_reports()
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Incident):
            self.__queue.append(other)
        return self.prioritize_reports()

    def __call__(self, incident_id):
        for incident in self.__queue:
            if incident.id == incident_id:
                return incident
            pass
        raise ValueError("No incident found with the given ID")

    def __lt__(self, other):
        return len(self.__queue) < len(other.__queue)

    def __gt__(self, other):
        return len(self.__queue) > len(other.__queue)

    def __bool__(self):
        return bool(self.__queue)

    def __len__(self):
        return len(self.__queue)
    
    #kolejka jest sortowana wg czasu, a pierwsze do rozdysponowania do 10min od zgłoszenia najstarszego także wg priorytetowości
    def prioritize_reports(self):
        if self.__queue: 
            #sortuje kolejke zgłoszeń po czasie zgłoszenia (od najstarszego do najnowszego)
            sorted_queue_by_time = sorted(self.__queue, key = lambda x: x.time_of_the_report)

            prioritized_queue = IncidentQueue()

            # wybieram zgłoszenia max. 10min nowszych od najstarszego z wysoką priorytetowością o ile ten pierwszy w kolejce nie ma wysokiej priorytetowości
            if "low" in sorted_queue_by_time[0].priority.lower():
                priority_reports = [incident for incident in sorted_queue_by_time[1:] 
                                    if incident.time_of_the_report <= sorted_queue_by_time[0].time_of_the_report + timedelta(minutes=10)
                                    and "high" in incident.priority.lower()]
                # ustawienie zgłoszeń z większą priorytetowością na początek kolejki i usunięcie ich ze starej kolejki
                for incident in priority_reports:
                    prioritized_queue += incident
                    sorted_queue_by_time.remove(incident)
            else:
                pass

            #połczenie kolejek z posortowanymi zgłoszeniami
            prioritized_queue.__queue += sorted_queue_by_time

            return prioritized_queue
        else:
            return self




if __name__ == "__main__":
    queue = IncidentQueue()
    incident1 = Incident("Power outage in sector 4", "Low", "9.37 PM", (50.095340, 19.920282), "-", "New")
    incident2 = Incident("Power outage in White House", "High", "9.38 PM", (50.095340, 19.920282), "-", "New")
    incident3 = Incident("Fire alarm in building 21", "High", "1.38 AM", (50.095340, 19.920282), "-", "New")
    incident4 = Incident("Fire alarm in building 22", "High", "1.32 AM", (50.095340, 19.920282), "-", "New")
    incident5 = Incident("Power outage in sector 7", "Low", "1.28 AM", (50.095340, 19.920282), "-", "New")
    incident6 = Incident("Fire alarm in building 129", "High", "8.15 AM", (50.095340, 19.920282), "-", "New")

    print(f"---------- wyświetlanie za pomocą __str__ ----------")
    print(queue)

    print(f"---------- dodanie za pomocą __iadd__ ----------")
    queue += incident1
    queue += incident2
    queue += incident3
    queue += incident4
    print(queue)
    print(f"---------- dodanie za pomocą __add__ ----------")
    queue = queue + incident5
    queue = queue + incident6
    print(queue)

    print(f"---------- dostęp za pomocą __getitem__ ----------")
    print(queue[0])
    print(f"---------- sprawdzenie za pomocą __contains__ ----------")
    print(incident1 in queue)

    print(f"---------- iteracja za pomocą __iter__ i __next__ ----------")
    for incident in queue:
        print(incident)

    print(f"---------- dodawanie prawostronne za pomocą __radd__ ----------")
    new_incident = Incident("Test incident", "Low", "7.15 PM", (50.095340, 19.920282), "-", "New")
    queue = new_incident + queue

    print(f"---------- test za pomocą __bool__ ----------")
    if queue:
        print("Queue is not empty.")

    print(f"---------- długość kolejki za pomocą __len__ ----------")
    print(len(queue))

    print(f"---------- wyszukiwanie za pomocą __call__ ----------")
    print(queue(1))

    print(f"---------- posortowana kolejka----------")
    # print(dir(queue))
    print(queue)
    print(queue[0])
    