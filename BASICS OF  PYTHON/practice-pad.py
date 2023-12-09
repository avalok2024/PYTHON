class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person('jhon',36) 
print(p1)
# print(p1.name)
# print(p1.age)
