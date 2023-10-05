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
