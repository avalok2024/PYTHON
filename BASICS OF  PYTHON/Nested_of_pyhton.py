# nested loop using the if and else

'''which number is hightest number a , b and c'''

def  numbers(a, b , c):
    if a > b :
        if a > c: 
            print("a is the greatest number!")
        else:
            print("c is the gratest number! ")
    elif b > c :
        if b > a :
            print("b is the greatest number!")
        else:
            print("a is the greatest number")
    else:
        print("c is the greatest number")

numbers(1,2,3)

    

