import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"Guess the Number in between 1 to {x} : "))
        if guess < random_number: 
            print("sorry, guess again, Too low!")
        elif guess > random_number:
            print("Sorry!, guess again, Too High")
    print("Yah, congragtes! you guess the correct number {}".format(random_number))


def computer_guess(x):
    low = 1 
    high = x 
    feedback = ""
    while feedback != "c" and low != high:
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high(H) , too low(L), or correct(C) : ")
        if feedback == "h":
            guess = high - 1 
        elif feedback == "l":
            guess = low + 1 
    print(f"Yah, the computer guess the your number,{guess}, correctly")

computer_guess(10)