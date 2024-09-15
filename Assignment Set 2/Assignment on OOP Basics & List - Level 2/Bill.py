
class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id = bill_id
        self.__patient_name = patient_name
        self.__bill_amount = 0

    def get_bill_id(self): return self.__bill_id
    def get_patient_name(self): return self.__patient_name
    def get_bill_amount(self): return self.__bill_amount

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        self.__bill_amount += consultation_fees
        for index, quantity in enumerate(quantity_list):
            self.__bill_amount += quantity * price_list[index]
        return self.__bill_amount

bill = Bill(101, "John")
bill.calculate_bill_amount(1000, [1, 2, 3], [10, 20, 30])
print(bill.get_bill_amount())