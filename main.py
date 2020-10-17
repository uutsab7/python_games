import random
lst=['s','p','r']
chance=3
no_of_chance=0
computer_point=0
timro_point=0

print("\t \t \t \t  scissor,paper rock game \n\n")
print(" s for scissor \n p for paper \n r for rock \n")

while(no_of_chance < chance):
    _input= input("Scissor,Paper,Rock:")
    _random= random.choice(lst)

    if(_input==_random):
            print("its a tie bro no one wins lol ")

    elif(_input=="p" and _random=="s"):
            computer_point=computer_point+1
            print(f"your guess is {_input} and computer guess is {_random} \n ")
            print("computer wins 1 point \n")
            print(f"computer_point is {computer_point} your point is {timro_point} \n")

    elif(_input=="p" and _random=="r"):
            timro_point=timro_point+1
            print(f"your guess is {_input} and computer guess is {_random} \ n")
            print("you win 1 point")
            print("computer_point is {computer_point} and your point is {timro_point} \n")

    elif(_input=="s" and _random=="p"):
            timro_point=timro_point+1
            print(f"your guess is {_input} and computer guess is {_random} \ n")
            print("you win 1 point")
            print("computer_point is {computer_point} and your point is {timro_point} \n")

    elif (_input == "s" and _random == "r"):
            computer_point=computer_point+1
            print(f"your guess is {_input} and computer guess is {_random} \ n")
            print("computer win 1 point")
            print("computer_point is {computer_point} and your point is {timro_point} \n")

    elif (_input == "r" and _random == "s"):
            timro_point=timro_point+1
            print(f"your guess is {_input} and computer guess is {_random} \ n")
            print("you win 1 point")
            print("computer_point is {computer_point} and your point is {timro_point} \n")

    elif (_input == "r" and _random == "p"):
             computer_point=computer_point+1
             print(f"your guess is {_input} and computer guess is {_random} \ n")
             print("computer win 1 point")
             print("computer_point is {computer_psoint} and your point is {timro_point} \n")

    else:
              print("bro its a wrong input \n")

    no_of_chance=no_of_chance+1
    print(f"{chance - no_of_chance} turn  is left out of {chance}  for you now\n")

print("game over")


if(computer_point==timro_point):
    print("tie bhayo")

elif(computer_point > timro_point):
    print("computer wins you loose ")

else:
    print("you won computer loose")

print(f"your point is {timro_point} and computer point is {computer_point}")