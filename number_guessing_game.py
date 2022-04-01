import random 
print ("__"*60)
print()
print('Hello Guys This is number guessing Game between 1 to 50 You will get five chance to guess the correct number : '.title().center(120))
print("__"*60)

cg_number  = random.randint(1,50)
num = 1

while num <= 5:
    f_number = int(input(f"Enter the {num} number : ".rjust(70)))
    if f_number > 50 or f_number < 0:
        print("This is Out of range!!!".center(120))
        print("__"*60)
        continue
    else:
        if f_number == cg_number:
            print(f"Ohhh Great!! You are awesome you guessed {cg_number} correct ".center(120))
            break
        elif f_number > cg_number:
            print(f"You guessed {f_number} the Higher Please guess lower number ".center(120))
            print("__"*60)
        else:
            print(f"You guessed {f_number} the lower number please guess higher number ".center(120))
            print("__"*60)
        num += 1
else:
    print("You are such a looeser!!!!".center(120))
    print(f"The Number was {cg_number}".center(120))
        