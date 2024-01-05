from item import Item
from keyboard import keyboard
item1 = keyboard("avkeyboard", 750)

item1.apply_incriment(0.2)
item1.apply_discount()
print(item1.price)
