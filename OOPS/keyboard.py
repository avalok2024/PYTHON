from item import Item

class keyboard(Item):
    def __init__(self, name: str, price: float, quantity=0, broke_phone=1):
        # calling to super funtion for access the all the attribute/methods
        super().__init__(
            name, price, quantity
        )
