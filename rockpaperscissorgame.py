#project #3 
#Rock paper scissors game

import random
choices='rock','paper','scissor'

computer=random.choice(choices)
print("Welcome! to rock paper scissors game🐍")
while True:
 user=input("Enter your preference🙂:").lower()
 print("you chose💀:",user)
 print("computer chose☠️:",computer)
 if user == computer:
        print("Tie!" )
        computer=random.choice(choices)
        
 elif user == "rock" and computer == "scissor" or \
         user == "paper" and computer == "rock" or \
         user == "scissor" and computer == "paper" :
             print("You won!🫡")
             
 elif user in choices :
        print("Computer wins!😣")
 else:
     print("INVALID CHOICE!🤨")
     continue
 again=input("Wanna play again?🫥\nYES/NO:").lower()
 if again != "yes" : 
     print("THANKS FOR PLAYING!🫠")
     break  
