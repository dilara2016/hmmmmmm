import random#importing module
playing = True#initilise
number = str(random.randint(90,100)) # random built-in function
print("i will generate a number from 90 to 100,and you have to guess the number one digit at a time.")
print("the game ends when you get 1 hero")
while playing:
    guess = input("give me youre best guess! \n")
    if number == guess:
       print("you win the game YAY :]")
       print("the number was", number)
       break

    else:
     print("YOU DID NOT GUESS RIGHT. \n")