
import random
import time

number = random.randint(1,100)

def intro():
    print("May I ask you for your name?") 
    global name 
    name = input() 
    print( name +" we are going to play a game. I am thinking of a number 1 and 100")
    if(number%2==0):
          x = 'even'
    else:
         x = 'odd'
    print("/nThisis an {} number". format(x))
    time.sleep(.5)
    print("go ahead and guess!")

def pick():
     guessTaken = 0 
     while guessTaken < 6:
        time.sleep(.25)
        enter = input("Guess:")
        try:
             guess = int(enter)
             if guess <= 100 and guess >= 1:
                guessTaken += 1
                if guessTaken < 6:
                    if guess < number:
                        print("The guess of the number is too low ")
                    if guess > number:
                        print("The guess of the number is too high ")
                    if guess != number:
                        time.sleep(.5)
                        print("try again")
                    if guess == number:
                        break 
             if guess >= 100 and guess <= 1:
                print("enter the number in the range provided")
                time.sleep(.25)
        except: 
            print("I don't think that's a number"+enter+"is a number")
     if guess == number:
         guessTaken = str(guessTaken)
         print("Good job!{} guessed it in {} many guesses".format(name,guessTaken))
     if guess != number:
         print("nope. the number is "+ str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y":
    intro()
    pick()
    print("Do you want to play again")
    playagain = input()

    


                    
                

