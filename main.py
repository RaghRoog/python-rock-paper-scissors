import random

print("This is rock, paper scissors game.\n")
print("Press 1 to see rules\n")
print("Press 2 to play\n")
playerSelection = int(input())

if playerSelection == 1:
    print("Rules:\n")
    print("Rock vs paper --> paper wins\n")
    print("Rock vs scissors --> rock wins\n")
    print("Paper vs scissors --> scissors wins\n")
    print("To win you need to colect 3 points (win 3 rounds)\n")
elif playerSelection == 2:
    possibleSelecetions = ["rock", "paper", "scissors"]
    cpuSelection = random.choice(possibleSelecetions)
    print("1. Rock\n2. Paper\n3. Scissors")
    playerSelection = possibleSelecetions[int(input("Select move:\n"))-1]
    if ((playerSelection == "rock" and cpuSelection == "scissors") or
        (playerSelection == "paper" and cpuSelection == "rock") or
        (playerSelection == "scissors" and cpuSelection == "paper")):
            print("You: " + playerSelection + " vs CPU: " + cpuSelection)
            print("You won")
    elif ((playerSelection == "rock" and cpuSelection == "paper") or
          (playerSelection == "paper" and cpuSelection == "scissors") or
          (playerSelection == "scissors" and cpuSelection == "rock")):
            print("You: " + playerSelection + " vs CPU: " + cpuSelection)
            print("You lost")
