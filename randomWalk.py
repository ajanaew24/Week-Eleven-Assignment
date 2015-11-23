# Basic Structure for a Random Walk simulation
# Alicia Williams
# CIS-125 FA 2015
# Week 11: randomWalk.py
# Collaborated with Ethan Richards
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

#define startRange, endRange, stepRange
startRange = 100
endRange = 1000
stepRange = 10

def main():
    printHeader()
    for n in range(startRange,endRange,stepRange):
        averageDistance = getRandomWalk(n) #average distance given number of steps
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("Prediction of steps from starting point using a fair coin:")

#function to randomize heads or tails in a fair coin and return the total displacement
def getRandomWalk(steps):
    displacement = 0 #initial value
    for flip in range(steps):
        coin = random.randint(0,1) #coin flip for heads or tails
        if coin == 1:
            displacement = displacement + 1 #walk forwards one step
        else:
            displacement = displacement - 1 #walk backwards one step
    return displacement #returns total displacement of forwards and backwards walking

if __name__ == "__main__":
    main()