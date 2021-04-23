import random

def cpuMove():
    cpuMoveList = ["rock", "paper", "scissors"]
    cpuChoice = random.randint(0,2)
    return cpuMoveList[cpuChoice]

def play():
        userMove = input("Input your choice; rock, paper, or scissors\n Your Choice is ").lower()
        if userMove == "rock" or userMove =="paper" or userMove == "scissors":
            cpuChoice = cpuMove()
            print("The computer Chose: " + cpuChoice)
            if userMove == cpuChoice:
                print("Tie")
            elif cpuChoice == "rock" and userMove == "scissors":
                print("The Computer won!")
            elif cpuChoice == "paper" and userMove == "rock":
                print("The Computer won!")
            elif cpuChoice == "scissors" and userMove == "paper":
                print("The Computer won!")
            else:
                print("You Won!")
        else:
            print("You did not enter a valid move")
        
if __name__ == "__main__":
    print("Welcome To Rock Paper Scissors")
    playgame = input("Enter play or exit:  ").lower()
    while playgame =="play":
        play()
        playgame = input("Play again ? Play or Exit ").lower()
        if playgame == "exit":
            break