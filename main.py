#Guessing Game
from random import randint

random_number = randint(1,10)
guess = None

while True:
    guess = int(input("pic a number from 1-10: "))
    if guess < random_number:  
      print("Too Low!")
    elif guess > random_number:
      print("Too High!")
    else:
      print("You Won!!!")
      play_again = input("Do you want to play again? (y/n) :")
      if play_again == "y":
        random_number = randint(1,10)
        guess = None
      else:
        print("Thanks for playing!")
        break
