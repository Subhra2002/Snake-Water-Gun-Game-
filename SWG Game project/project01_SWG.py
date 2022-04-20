import random


def game(computer,user):
    if computer == user:
        return None
    elif computer == "s":
        if user == "w":
            return False
        elif user == "g":
            return True
    elif computer == "w":
        if user == "g":
            return False
        elif user == "s":
            return True
    elif computer == "g":
        if user == "s":
            return False
        elif user == "w":
            return True







print("Computer turn : Snake(s) , Water(w) , Gun(g) ?")
randomNO=random.randint(1,3)
# print(randomNO)
if randomNO == 1:
    computer = "s"
elif randomNO == 2:
    computer = "w"
elif randomNO == 3:
    computer = "g"

user = input("Yours turn :  Snake(s) , Water(w) , Gun(g) ?")

a = game(computer,user)

print(f"Computer chose {computer}")
print(f"user chose {user}")
if a == None:
    print("The match is tie")
elif a :
    print("You Win")
else:
    print("You Loose")
     