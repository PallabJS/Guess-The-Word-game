import time
import random
import sys
#================================ GAME SETUP ================================
# List for tracking correct letters guessed
reveal = []
score = 0
# Variable for enabling chosing of replay
key = 'k'
print("\n")
print("==============   GUESS THE WORD - GAME   ==============\n\t\t By Pallab Jyoti Singha\n")
player = input("Tell me your name: ")
print("Hello", player)
print("Wait a sec, while I set up a word for you")

# Beautifying Game Loading
for i in range(0,15):
    time.sleep(0.2)
    sys.stdout.flush()
    print(" - ", end="")
print("\nDONE SETUP")
time.sleep(1.5)

# Word Selection from the file
fp = open("words.txt", "r")
data = fp.read()
words = data.split(" ")
word = list(words[random.randrange(0,35)].upper())
fp.close()
print("I have set a word of length = ", len(word))

# Setting up reveal list with same number of '-' elements as the word 
for i in range(0, len(word)):
    reveal.append("-")
print(reveal)

# Setting Max attempts for Wordlength minus 1
attempts = len(word)-1
print("Wrong Attempts =", int(attempts))

#================================ GAME LOGIC ================================
#-------------------------------- Reset Game Variables ----------------------
def gameReset():
    global word
    global reveal
    global attempts
    global key
    key = 'k'
    
    # Word selection from file
    fp = open("words.txt", "r")
    data = fp.read()
    words = data.split(" ")
    print("Let's set up a word for you")
    word = list(words[random.randrange(0,35)].upper())
    fp.close()
    reveal = []

    # Setting up reveal list with same number of '-' elements as the word
    for i in range(0, len(word)):
        reveal.append("-")
    print(reveal)
    attempts = len(word)-1

    # Calling one Game Round
    loopGame()

#-------------------------------- Function for Game Replay ----------------------
def replay():
    global key
    print("Do you want to play again? Y/N : ", end = "")
    key = input()
    if key=='Y' or key=='y':
        print("\n")
        gameReset()
    elif key=='n' or key=='N':
        print("Well then, See you again.")
        exit(0)
    else:
        print("What was that?, Try again.")
        replay()
        
#-------------------------------- Main Game Logic ----------------------
def loopGame():
    called = []
    global word
    global reveal
    global attempts
    global key
    global score
    key = 'k'
    exitflag = False
    print("\t\t\t<LET'S START>")
    while(attempts>0):
                
        guess = input("Guess a letter: ")
        guess = guess.capitalize()

        # CHECK FOR SAME LETTER ENTRY
        if guess not in called:

        # LOGIC FOR LETTER MATCH
            if guess in word:
                print("Guess Matched")
                valueindex = 0
                for i in word:
                    if i==guess:
                        reveal[valueindex]=guess
                    valueindex = valueindex+1
                print("reveal:", reveal)
                print("\n")
            else:
                attempts = attempts-1
                if attempts>=0:
                    print("WRONG GUESS, Remaining Attempts: ", int(attempts))
        # LOSING STATEMENT
                if attempts==0:
                    print("You have Lost the Game!")
                    score = 0
                    replay()
                    break                       
            called.append(guess)
        else:
            print("Already Called for ", guess, "Try Another")  

        # WINNING STATEMENT
        if "-" not in reveal:
            print("The word is", "".join(word), "\nYOU WON!!!")
            score = score + 1
            print("CURRENT SCORE =", score)
            if score == 2:
                print(">> Well Done")
            elif score == 3:
                print(">>> Great")                
            elif score == 4:
                print(">>>> Excellent")
            elif score == 5:
                print(">>>>> You are a Hero")
            elif score == 6:
                print(">>>>>> Pro in word Guessing")
                print("Next is the final guess!")
            elif score>6:
                print("Congrats! YOU ARE NOW A LEGEND")
                sys.exit()
            replay()
            break
#=============================================================================
loopGame()