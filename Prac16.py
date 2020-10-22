#rock paper scissors
print('''
Instructions:
Enter your choice - Rock, Paper or scissors.
You will get a +1 for each win and -1 for each loose.
If your score reaches -5, you lose ,and if +5, you win.
'''
list_of_options=["Rock", "Paper", "Scissors"]
import random
player_score=0
player = True
while player == True:
 user_input= input("Enter your choice: ").upper()
 random_option= random.randrange(0, 3)
 computer_option= list_of_options[random_option].upper()
 print(f"Computer: {computer_option}")
 if (user_input == "ROCK") and (computer_option == "PAPER"):
     print("Computer wins!!")
     player_score -= 1
 elif (user_input == "ROCK") and (computer_option == "SCISSORS"):
     print("You win!!")
     player_score += 1
 elif (user_input == "PAPER") and (computer_option == "ROCK"):
     print("You win!!")
     player_score += 1
 elif (user_input == "PAPER") and (computer_option == "SCISSORS"):
     print("Computer wins!!")
     player_score -= 1
 elif (user_input == "SCISSORS") and (computer_option == "ROCK"):
     print("Computer wins!!")
     player_score -= 1
 elif (user_input == "SCISSORS") and (computer_option == "PAPER"):
     print("You win!!")
     player_score += 1
 else:
     print("Tie!!")
 print(f"Your Score: {player_score}\n")
 if player_score < -5:
     print("You Lose!")
     player = False
 elif player_score > 5:
     print("You Win!")
     player = False
