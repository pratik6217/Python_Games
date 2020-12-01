import random 

def even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def prime(num):
    for i in range(2,num):
        if num % i == 0 and i == num:
            return "Prime"
        else:
            return "Not a prime"


def hint(guessed_no, actual_no):
    less_than = ["Your guess is too low", "Please raise your guess", "You are guessing too low", "You can go more higher and remmber the starting hint."]
    greater_than = ["Ohh that's way too high !", "Please lower your expectations...", "Your guess is way too high and remember the starting hint."]
    if (guessed_no) < actual_no:
        return random.choice(less_than)
    else:
        return random.choice(greater_than)


def guess_game():
    print("Welcome to Guess the number game:\nIn this game you just have to guess the number.....so let's begin with it: ")
    print("Please enter the difficulty level:\n1.Easy - Between 1 to 10\n2.Medium - Between 11 to 100\n3.Hard - between 101 and 1000" )
    while True:
        choice = input()
        if choice == "1" or choice.lower() == "easy":
            actual_no = random.randint(0,10) 
            break
        elif choice == "2" or choice.lower() == "medium":
            actual_no = random.randint(11,100)
            break 
        elif choice == "3" or choice.lower() == "hard":
            actual_no = random.randint(101,1000)
            break
        else:
            print("Please enter correct choice !")
        
    print("Let the guessing begin:")
    gen = random.choice([even(actual_no),prime(actual_no)])
    print("Here's a small hint for you to start with:\nThe number is a {hint} number.".format(hint=gen))
    while True:
        print("Enter your guess :")
        try:
            guessed_no = int(input())
            if guessed_no == actual_no:
                print("Your guess was correct.")
                break
            else:
                hi = hint(guessed_no, actual_no)
                print("Please try again !")
                print(hi)
        except ValueError:
            print("Please enter a valid number !")
    print("Thankyou for playing.... :)")

guess_game()
