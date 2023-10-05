import random

isLooped = True

while(isLooped):
    print("This is rock, paper scissors game.")
    print("Press 1 to see rules")
    print("Press 2 to play")
    print("Press 3 to exit")
    playerSelection = int(input())

    if playerSelection == 1:
        print("Rules:")
        print("Rock vs paper --> paper wins")
        print("Rock vs scissors --> rock wins")
        print("Paper vs scissors --> scissors wins")
        print("To win you need to colect 3 points (win 3 rounds)")
    elif playerSelection == 2:
        gameLoop = True
        cpuPoints = 0
        playerPoints = 0
        possibleSelecetions = ["rock", "paper", "scissors"]
        while(gameLoop):
            cpuSelection = random.choice(possibleSelecetions)
            print("1. Rock\n2. Paper\n3. Scissors")
            playerSelection = possibleSelecetions[int(input("Select move: "))-1]
            if ((playerSelection == "rock" and cpuSelection == "scissors") or
                (playerSelection == "paper" and cpuSelection == "rock") or
                (playerSelection == "scissors" and cpuSelection == "paper")):
                    print("You: " + playerSelection + " vs CPU: " + cpuSelection)
                    print("You won this round")
                    playerPoints += 1
            elif ((playerSelection == "rock" and cpuSelection == "paper") or
                  (playerSelection == "paper" and cpuSelection == "scissors") or
                  (playerSelection == "scissors" and cpuSelection == "rock")):
                    print("You: " + playerSelection + " vs CPU: " + cpuSelection)
                    print("You lost")
                    cpuPoints += 1
            print("Your points: " + str(playerPoints) + " CPU points: " + str(cpuPoints))
            if playerPoints == 3 or cpuPoints == 3:
                gameLoop = False
    elif playerSelection == 3:
        isLooped = False