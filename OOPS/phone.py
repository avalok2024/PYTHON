from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broke_phone=1):
        # calling to super funtion for access the all the attribute/methods
        super().__init__(
            name, price, quantity
        )
        # Run validation for values
        assert broke_phone >= 0, f"Broken Phone {broke_phone} is not greater than or equal to zero"

        # Assigning the self value
        self.broken_phone = broke_phone
