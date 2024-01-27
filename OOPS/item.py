import csv

class Item:
    pay_rate = 0.8  # The Pay rate after 20%
    all = []

    def calculate_the_total(self):
        return self.__price * self.quantity

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation for values
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assigning the self value
        self.__name = name
        self.quantity = quantity
        self.__price = price

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_incriment(self, incriment_value):
        self.__price = self.__price + self.__price * incriment_value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is so long")
        else:
            self.__name = value


    @classmethod

    def instance_from_csv(cls):
        with open("itmes.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        # for item in items:
        #     Item(
        #         name=item.get("name"),
        #         price=int(item.get("price")),
        #         quantity=int(item.get("quantity")),
        #     )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            # check the also included the 7.0 as float
            return True
        else:
            return False



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

# Using it
    
item = Item("Capain av alok",3)
print(item.name)