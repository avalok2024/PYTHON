# Creating the varibles which we want for id card 

Name = input("Full Name  :")
Fathers = input("Fatheres Name : ")
Id = int(input("Roll no. :"))
Date_of_birth = input("Date of Birth : ")
collage = input("Name of collage :")

# Creating a output in formate of Id card like
print( " \n ")
id_card = f'''Name : {Name} \nFather's Name : {Fathers} \nDate of Birth : {Date_of_birth} \nRoll.no : {Id} \nCollage : {collage}'''

print(id_card)

