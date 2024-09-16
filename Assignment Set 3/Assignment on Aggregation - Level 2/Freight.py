class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        customer_id = str(self.__customer_id)
        return not (len(customer_id) != 6 or customer_id[0] != "1")


class Freight:
    counter = None

    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__freight_id = None
        self.__freight_charge = None
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance

    def get_freight_charge(self):
        return self.__freight_charge

    def get_freight_id(self):
        return self.__freight_id

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_from_customer(self):
        return self.__from_customer

    def get_recipient_customer(self):
        return self.__recipient_customer

    def validate_weight(self):
        return self.__weight % 5 == 0

    def validate_distance(self):
        return 5000 >= self.__distance and self.__distance >= 500

    def forward_cargo(self):
        if (
            not self.validate_weight()
            or not self.validate_distance()
            or not self.__recipient_customer.validate_customer_id()
            or not self.__from_customer.validate_customer_id()
        ):
            self.__freight_charge = 0
            return False

        if Freight.counter == None:
            Freight.counter = 198
        else:
            Freight.counter += 1

        self.__freight_id = 200 + 2 * (Freight.counter - 198)

        self.__freight_charge = self.__weight * 150 + self.__distance * 60
        return True


"""
Customer(customer_id:112345 , 
    customer_name:jill , 
    address:Chennai),
    weight-875,
    distance-5000,
    counter-198
(Method invoked 5 times) 
"""


def printer(obj):
    obj.forward_cargo()
    print("id: ", obj.get_freight_id())
    print("Count: ", Freight.counter)


printer(
    Freight(
        Customer(112345, "jill", "Chennai"),
        Customer(112345, "jill", "Chennai"),
        875,
        5000,
    )
)
printer(
    Freight(
        Customer(112345, "jill", "Chennai"),
        Customer(112345, "jill", "Chennai"),
        875,
        5000,
    )
)
printer(
    Freight(
        Customer(112345, "jill", "Chennai"),
        Customer(112345, "jill", "Chennai"),
        875,
        5000,
    )
)
printer(
    Freight(
        Customer(112345, "jill", "Chennai"),
        Customer(112345, "jill", "Chennai"),
        875,
        5000,
    )
)
printer(
    Freight(
        Customer(112345, "jill", "Chennai"),
        Customer(112345, "jill", "Chennai"),
        875,
        5000,
    )
)
