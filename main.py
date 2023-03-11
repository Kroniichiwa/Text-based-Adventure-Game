import random
import sys
#Text-based Adventure Game: Develop a simple text-based game that allows the user to navigate through a series of rooms and solve puzzles.

###################
#                 #
#                 #
#        𖨆        #
#                 #
#                 #
###################

# min from 0,0 ---> max at 5,5 
# 50% you will find a quizz ( If your answer is wrong then you move back! )
# if you find a chest you win!

position_Y = 3
position_X = 9
movetime = 0
win = 0

questions_list = {
    "What is the capital of France?" : "Paris",
    "What is the largest planet in our solar system?" : "Jupiter",
    "How many sides does a triangle have?" : "3",
    "What is the color of a banana?" : "Yellow",
    "What is the opposite of hot?" : "Cold",
    "What is the smallest prime number?" : "2",
    "What is the chemical symbol for water?" : "H2O",
    "What is the name of the famous detective created by Sir Arthur Conan Doyle?" : "Sherlock Holmes",
    "What is the most commonly used programming language?" : "Python",
    "What is the capital of Japan?" : "Tokyo"
}


def quizz():
    #handle UnboundLocalError
    global movetime
    global win

    chance = random.randint(1,10)
    if chance < 10 and chance > 8 :
        askQuestion()
    elif chance == 10 :
        print("_"*50)
        print("You find the chest!")
        print(f"Congratulations your win the game with {movetime} moves!")
        sys.exit()
    else :
        win = 1
    movetime += 1

def askQuestion():
    #handle UnboundLocalError
    global win
    # Select a random question from the dictionary
    question = random.choice(list(questions_list.keys()))

    # Ask the user the selected question
    print("_"*50)
    print("You have met a very wise man, answer this question.")
    user_answer = input(question + " ").lower()

    # Check if the user's answer is correct or not
    if user_answer == questions_list[question].lower():
        print("_"*50)
        print("Correct! You can move now!")
        win = 1 
    else:
        print("_"*50)
        print("Incorrect. The correct answer is", questions_list[question])
        print("Go back!")
        win = 0



def location(move):
    global win
    global position_X
    global position_Y

    if move == "R":
        #print("_____________________",position_X)
        if position_X == 16:
            print("You can't go right anymore")
        else:
            quizz()
            if win == 1:
                position_X += 1
                win = 0
    elif move == "L":
        if position_X == 1:
            print("You can't go left anymore")
        else:
            quizz()
            if win == 1:
                position_X -= 1
                win = 0
    elif move == "T":
        if position_Y == 0:
            print("You can't go up anymore")
        else:
            quizz()
            if win == 1:
                position_Y -= 1
                win = 0
    elif move == "B":
        #print("_____________________",position_Y)
        if position_Y == 4:
            print("You can't go down anymore")
        else:
            quizz()
            if win == 1:
                position_Y += 1
                win = 0
    else:
        print("Please only type R, L, B, or T")



def main():
    #handle UnboundLocalError
    global position_X
    global position_Y
    while True :
        #strat edge
        print("####################")
        y = 0
        x = 0
        while y < 5 :
            print("#",end='')
            while x < 18 :
                if position_X == x and position_Y == y  :
                    print("𖨆",end='')
                else :
                    print(" ",end='')
                x+=1
            print("#")
            y+=1
            x = 0

        #end edge
        print("####################")

        print("Move your charecter 𖨆 ")
        move = input("Left = L , Right = R, Bottom = B, Top = T : ").upper()
        location(move)


if __name__ == '__main__':
    print("Welcome to the Adventure game!")
    main()
