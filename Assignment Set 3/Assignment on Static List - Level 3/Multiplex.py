# lex_auth_012751902958862336276
class Multiplex:
    __list_movie_name = ["movie1", "movie2"]
    __list_total_tickets = [100, 60]
    __list_last_seat_number = [None, None]
    __list_ticket_price = [150, 200]

    def __init__(self):
        self.__seat_numbers = None
        self.__total_price = None

    def calculate_ticket_price(self, movie_index, number_of_tickets):
        self.__total_price = (
            Multiplex.__list_ticket_price[movie_index] * number_of_tickets
        )

    def check_seat_availability(self, movie_index, number_of_tickets):
        if Multiplex.__list_total_tickets[movie_index] < number_of_tickets:
            return False
        else:
            return True

    def get_total_price(self):
        return self.__total_price

    def get_seat_numbers(self):
        return self.__seat_numbers

    def book_ticket(self, movie_name, number_of_tickets):

        if movie_name not in self.__list_movie_name:
            return 0
        movie_index = 0 if movie_name == "movie1" else 1

        generated_list = None
        generated_list = self.generate_seat_number(movie_index, number_of_tickets)

        if generated_list == -1:
            return -1
        
        self.__seat_numbers = generated_list
        self.calculate_ticket_price(movie_index, number_of_tickets)
        

    def generate_seat_number(self, movie_index, number_of_tickets):
        prefix = 'M1-' if movie_index == 0 else 'M2-'
        if not self.check_seat_availability(movie_index, number_of_tickets):
            return -1

        self.__list_total_tickets[movie_index] -= number_of_tickets

        generated_tickets = []
        start = None
        if self.__list_last_seat_number[movie_index] == None:
            start = 1
        else:
            start = int(self.__list_last_seat_number[movie_index].split("-")[1]) + 1
        generated_tickets = [f'{prefix}{i}' for i in range(start, number_of_tickets + start)]

        self.__list_last_seat_number = generated_tickets[-1]

        return generated_tickets



booking1 = Multiplex()
status = booking1.book_ticket("movie1", 5)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2 = Multiplex()
status = booking2.book_ticket("movie2", 6)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
