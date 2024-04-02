import random

#intro
def intro():
  name = input("Please, enter your name: " )
  if len(name)<3:
    print("Name must be 3 characters")
    intro()
  elif len(name)>50:
    print("Name must be at most 50 characters")
    intro()
  else:
    print('Hi ' + name  + " welcome to our Gaming club")
    print("Here is the games for you. Please choose one!")

  return name 

intro()

#random
def randomize():
    numbers = (0,1,2,3,4,5,6,7,8,9,10)
    secret = random.choice(numbers)
    return secret

secret = randomize()

#GuessGame
def guess_game():
    print("You successfully started Guess Game")
    print("Guess the number(1-10)")
    chance = 0
    chance_limit = 3
    while chance < chance_limit:
        guess = input("Guess: ")
        if guess.isdecimal() and (int(guess)>=0 and int(guess)<=10):
          guess = int()
          chance += 1
          if guess == secret:
            print ("Game over. You won")
            break
          else:
            print ("You failed. Please try again")
        else:
          print("You entered false value enter again. Please try again")
    return ask_user()

          
#TrackDelivery
def track_delivery():
    command = " "
    while command.lower != "quit":
      command = input("> ").lower()
      if command == "start" :
        delivery = input("What do you want for delivery?(anything) " )
        input("Adress: ")
        print(delivery + " is on the way")
        print("it will take almost 5 working days to be delivered")
      elif command == "cancel":
        print("Delivery cancelled.")
      elif command == "help":
        print("""
        start - to start the delivery
        status - to check status
        cancel - to cancel delivery
        quit - to go to the menu 
        """)
      elif command == "status":
        print( str(secret) + " days left to go to the destination")
      elif command == "quit":
        ask_user()
      else:
        print("I don't understand that")

#Selection
def ask_user():
    print("Track Delivery \nGuess Game ")
    response = ''
    while response not in {"t", "g"}:
        response = input("Please enter t to play Track Deliver or g to enjoy Guess Game ").lower()
        if response == "t":
            track_delivery()
        elif response == "g":
            guess_game()
    return response == "t"

ask_user()




    









