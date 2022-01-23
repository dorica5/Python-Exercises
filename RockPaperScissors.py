import random
the_options=["Rock","Paper","Scissors"]
count=1
comp_tally=0
user_tally=0
while True:
    print (f"Let's play round {count}")
    computer_choice= random.choice(the_options)
    users_choice= input("Your choice (Rock/Paper/Scissors)? ")
    
    if users_choice=="Rock" and computer_choice=="Scissors":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Human wins")
        user_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice=="Scissors" and computer_choice=="Rock":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Computer wins")
        comp_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice=="Paper" and computer_choice=="Rock":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Human wins")
        user_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice=="Rock" and computer_choice=="Paper":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Computer wins")
        comp_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice=="Scissors" and computer_choice=="Paper":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Human wins")
        user_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice=="Paper" and computer_choice=="Scissor":
        print(f"Human chose {users_choice},Computer chose {computer_choice}. Computer wins")
        comp_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    elif users_choice==computer_choice:
        print(f"Human chose {users_choice},Computer chose {computer_choice}. It's a tie")
        user_tally +=1 
        comp_tally +=1
        print(f"Score: human {user_tally}, computer {comp_tally}")
    choice= input("Do you wish to continue playing? (y/n)? ")
    if choice == "n":
        break
    count +=1
    
    
        