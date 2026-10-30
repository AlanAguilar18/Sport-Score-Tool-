"""
SPORT SCORER TOOL
Multi Sport Scorer
Author: Alan 
"""
"""
Context:
Every sport has a different form to score, so this program solves that by letting the user pick one sport of the options 
from the menu and loading a function with only that sport’s scoring rules, so it tracks the match correctly without 
the user having to remember them all.
"""
def menu():
    #It helps the user see the options it has to choose between
    print("Choose an option: ")
    print("1. Basketball")
    print("2. Tennis")
    print("3. Soccer")
    print("4. Football")

def options():
    #The function shows a menu that helps the user choose an option of the three
    print("Choose an option: ")
    print("1 → Player 1")
    print("2 → Player 2")
    print("3 → End")

def options_basketball():
    #It helps choosing the type of action it was on the game
    print("Choose an option: ")
    print("1. From the paint → 2 points")
    print("2. From the three point line → 3 points")
    print("3. Foul → 1 or 2 points")

def basketball():
    #It calculates the score of every shot made on court between 2 teams/individuals and can determine who wins or loses
    while True:
        game = [0,0]
        options()
        point = int(input("¿Who won the point? "))
        match point:
            case 1:
                options_basketball()
                canasta1 = int(input("¿What kind of action was it? "))
                match canasta1:
                    case 1:
                        game[point-1] += 2
                    case 2:
                        game[point-1] += 3
                    case 3:
                        foul = input("First shoot(1 → yes or 2 → no): ")
                        match foul:
                            case 1:
                                game[point-1] += 1
                            case 2:
                                print("Next time")
                            case _:
                                print("Invalid")
                        foul2 = input("Second shoot(1 → yes or 2 → no): ")
                        match foul2:
                            case 1:
                                game[point-1] += 1
                            case 2:
                                print("Really???")
                            case _:
                                print("Invalid")
                    case _:
                        print("Invalid")
                print_progress(game)
            case 2:
                options_basketball()
                canasta2 = int(input("¿What kind of action was it? "))
                match canasta2:
                    case 1:
                        game[point-1] += 2
                    case 2:
                        game[point-1] += 3
                    case 3:
                        foul1 = int(input("First shoot(1 → yes or 2 → no): "))
                        match foul1:
                            case 1:
                                game[point-1] += 1
                            case 2:
                                print("Good luck next time")
                        foul3 = int(input("Second shoot(1 → yes or 2 → no): "))
                        match foul3:
                            case 1:
                                game[point-1] += 1
                            case 2:
                                print("Really???")
                            case _:
                                print("Invalid")
                    case _:
                        print("Invalid, try again")
            case 3:
                break
            case _:
                print("Invalid, try again")
        print_progress(game)
    return(win(game))

def soccer():
    #It calculates the score of every goal between 2 teams and can determine who wins or loses
    goals = [0,0]
    while True:
        options()
        who = int(input("Which team scored: "))
        match who:
            case 1:
                goals[who-1] +=1
            case 2:
                goals[who-1] +=1
            case 3:
                break
            case _:
                print("Invalid")
        print_progress(goals)
    return(win(goals))

def tennis():
    #It calculates the score of every point made, the program also can dertermine when it is a game and a set between 2 individuals and can determine who wins or loses
    points = [0,0]
    games = [0,0]
    sets = int(input("Choose between a game of 3 or 5 sets: "))
    sets = [0,0]
    while True:
        options()
        point = int(input("Who won the point: "))
        match point:
            case 1:
                points[point-1] += 15
                if points[0] == 45:
                    points[0] -= 5
                elif points[0] == 55:
                    points[0] += 5
                print_progress(points)
                if points[0] == 60:
                    games[point-1] += 1
                    points = [0,0]
                    print_progress(games)
                    if games[0] == 6:
                        sets[point-1] += 1
                        games = [0,0]
                        print_progress(sets)
                        if sets[0] == sets:
                            break
            case 2:
                points[point-1] += 15
                print_progress(points)
                if points[1] == 45:
                    points[1] -= 5
                elif points[1] == 55:
                    points[1] += 5
                if points[1] == 60:
                    games[point-1] += 1
                    points = [0,0]
                    print_progress(games)
                    if games[1] == 6:
                        sets[point-1] += 1
                        games = [0,0]
                        print_progress(sets)
                        if sets[1] == sets:
                            break
            case 3:
                break
            case 4:
                print("Invalid, try again")
    return(win(points))

def print_progress(b):
    print(b[0],"/",b[1])

def win(a):
    #This function helps me simplifying in all the sports on the program to determine who is the winner
    if a[0] > a[1]:
        return("Player 1 won and Player 2 lost")
    elif a[1] > a[0]:
        return("Player 2 won and Player 1 lost")
    elif a[0] == a[1]:
        return("TIE")
    else:
        return("DNP")
        
def main():
    #The function helps organise all of the other functions into one
    menu()
    option = int(input("Choose: "))
    match option:
        case 1:
            print(basketball())
        case 2:
            print(tennis())
        case 3:
            print(soccer())
        case _:
            print("Invalid, try again")
main()
