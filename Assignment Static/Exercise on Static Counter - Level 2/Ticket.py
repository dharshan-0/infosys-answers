
class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__ticket_id = None
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination

    def get_ticket_id(self): return self.__ticket_id
    def get_passenger_name(self): return self.__passenger_name
    def get_source(self): return self.__source
    def get_destination(self): return self.__destination

    def validate_source_destination(self):
        if self.__source.upper() != 'DELHI'.upper() or self.__destination.upper() not in ['PUNE', 'MUMBAI', 'CHENNAI', 'KOLKATA']:
            return False
        return True
    
    def generate_ticket(self):
        if not self.validate_source_destination(): return False
        Ticket.counter += 1
        self.__ticket_id = f'{self.__source[0].upper()}{self.__destination[0].upper()}{Ticket.counter:02}'
