import random 

round = 3
while round:
    def play():
        user = input("what is your choice ? Scissors(S), Rock(R) and Paper(P) :")
        computer = random.choice(["r", "p", "s"])

        if user == computer:
            return "Tie!"
        
        if is_win(user, computer):
            return "You Win!"
        
        return "You Lost!"

    
    def is_win(player, opponet):
        if (player == "r" and opponet == "p") or (player == "p" and opponet == "s") or (player == "s" and opponet == "r"):
            return True 
        
        
    print(play())
    
