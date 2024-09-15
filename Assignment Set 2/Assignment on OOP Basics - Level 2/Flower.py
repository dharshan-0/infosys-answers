class Flower:
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None

    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name
    def get_flower_name(self): return self.__flower_name

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def get_price_per_kg(self): return self.__price_per_kg

    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
    def get_stock_available(self): return self.__stock_available

    def validate_flower(self):
        return self.__flower_name.upper() in ["ROSE", "ORCHID", "JASMINE"]

    def validate_stock(self, required_quantity):
        if self.__stock_available >= required_quantity:
            return True
        return False

    def sell_flower(self, required_quantity):
        if not self.validate_flower() or not self.validate_stock(required_quantity):
            return False
        self.__stock_available -= required_quantity
        return True
    
    def check_level(self):
        flower_levels = {
            "ORCHID": 15,
            "ROSE": 25,
            "JASMINE": 40
        }
        
        if not self.validate_flower():
            return False

        return self.__stock_available < flower_levels[self.__flower_name.upper()]

flower = Flower()
flower.set_flower_name("Rose")
flower.set_price_per_kg(200)
flower.set_stock_available(25)
print(flower.check_level())