import random
def guess_numbers():
    return random.randint(1,100) #randint is method
target_number=guess_numbers()
attempts=0


while True:
    user_guess=int(input("enter the number:"))
    attempts+=1

    if user_guess == target_number:
        print("congrats You guessed it right")
        break
    elif user_guess<target_number:
        print("try a higher number")
    else:
        print("Try a lower number")    
