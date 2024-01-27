class Item():
    pay_rate = 0.8
    all = []
    def __init__(self, name : str, price: float, quantity=0):
        assert price >= 0
        assert quantity >= 0

        self.__name = name 
        self.__price = price 
        self.quantity = quantity

        Item.all.append(self)
    
    @property 
    def price(self):
        return self.__name
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception ("This is too much small")
        else: 
            self.__name = value

item = Item('Captain av alok', 9000)
# item2 = Item("Rohan",9003,19)
# item._name = "srk"
print(item.name)

# print(item.price)
# print(item.quantity)
