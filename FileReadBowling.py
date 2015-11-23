#Alicia Williams
#CIS-125
#11/18/15
#Week 11 Assignment: FileReadBowling.py
#Collaborated with Ethan Richards

import string
#imports the game to play
from BowlingGame import Game
#opens testscores.txt as read only
filename = open("testscores.txt", "r")
gameList = []
#for loop to strip any bad characters in testscores and adds it to the list
for line in filename:
    lineScores = line.strip()
    gameList = line.split(",")
    gameList = [int(element) for element in gameList]
    #print(gameList)
    
    #separate the last element in each list
    FinalScore = gameList.pop()
    
    #create game
    newGame = Game()
    
    #rolls each roll and adds it to the score
    for pins in gameList:
        newGame.roll(pins)
    print("Given Final Score: ",FinalScore,"Actual Score: ",newGame.score(), "Score is Correct: ", FinalScore == newGame.score())