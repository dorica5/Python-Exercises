import random
while True:
    secret_number= random.randint(1,20)
    print("I am thinking of a number between 1 and 20")
    for guesstaken in range(1,7):

     
       x=int(input("Guess the number: "))
          break

        if x > secret_number:
            print("Your guess is too high")
            print("Take a guess:")

            break
        elif x<secret_number:
            print("Your guess is too low")
            print("Take a guess")
            break

        elif x==secret_number:
          print(f"Good job! You guessed my number in {guesstaken} guesses!")
        break
