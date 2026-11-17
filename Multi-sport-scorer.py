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
    print("4.End")

def options(name):
    #The function shows a menu that helps the user choose an option of the three
    print("Choose an option: ")
    print(f"1 → {name[0]}")
    print(f"2 → {name[1]}")
    print("3 → End")

def options_basketball():
    #It helps choosing the type of action it was on the game
    print("Choose an option: ")
    print("1. From the paint → 2 points")
    print("2. From the three point line → 3 points")
    print("3. Foul → 1 or 2 points")

def suma(a):
    Suma = []
    for i in a:
        total = 0
        for j in i:
            total += j
        Suma.append(total)
    return(Suma)

def basketball(name):
    #It calculates the score of every shot made on court between 2 teams/individuals and can determine who wins or loses
    game = [
        [0,0,0,0],
        [0,0,0,0]
        ]
    abc = abbreviations(name)
    i = 0
    while i < 4:
        while True:
            options(name)
            print("4 → Next quarter")
            print(" Q1|Q2|Q3|Q4")
            print_progress(game,abc)
            point = int(input("¿Who won the point? "))
            match point:
                case 1 | 2:
                    options_basketball()
                    canasta1 = int(input("¿What kind of action was it? "))
                    match canasta1:
                        case 1:
                            game[point-1][i] += 2
                        case 2:
                            game[point-1][i] += 3
                        case 3:
                            foul = int(input("First shoot(1 → yes or 2 → no): "))
                            match foul:
                                case 1:
                                    game[point-1][i] += 1
                                case 2:
                                    print("Next time")
                                case _:
                                    print("Invalid")
                            foul2 = int(input("Second shoot(1 → yes or 2 → no): "))
                            match foul2:
                                case 1:
                                    game[point-1][i] += 1
                                case 2:
                                    print("Really???")
                                case _:
                                    print("Invalid")
                        case _:
                            print("Invalid")
                case 3:
                    print(" Q1|Q2|Q3|Q4")
                    print_progress(game,abc)
                    print_progress(suma(game),abc)
                    return win(suma(game),name)
                case 4:
                    i += 1
                    if i == 4:
                        print(" Q1|Q2|Q3|Q4")
                        print_progress(game,abc)
                        print_progress(suma(game),abc)
                        return win(suma(game),name)
                case _:
                    print("Invalid, try again")
def soccer(name):
    #It calculates the score of every goal made between 2 teams/individuals and can determine who wins or loses
    goals = [
        [0,0],
        [0,0]
        ]
    abc = abbreviations(name)
    i = 0
    while i < 2:
        while True:
            options(name)
            print("4 → Half time")
            who = int(input("Which team scored: "))
            match who:
                case 1 | 2:
                    goals[who-1][i] +=1
                case 3:
                    print_progress(suma(goals),abc)
                    return(win(suma(goals),name))
                case 4:
                    i += 1
                    if i == 2:
                        print_progress(suma(goals),abc)
                        return(win(suma(goals),name))
                case _:
                    print("Invalid")
            print_progress(goals,abc)

def tennis(name):
    #It calculates the score of every point made, the program also can dertermine when it is a game and a set between 2 individuals and can determine who wins or loses
    points = [[0,0,0],
              [0,0,0]
              ]
    while True:
        sets = int(input("Choose between a game of 3 or 5 sets: "))
        if sets != 3 and sets != 5:
            print("Try again")
        else:
            break
    if sets == 3:
        sets = 2
    elif sets == 5:
        sets = 3
    abc = abbreviations(name)
    i = 0
    while points[0][2] < sets and points[1][2] < sets:
        options(name)
        point = int(input("Who won the point: "))
        match point:
            case 1 | 2:
                tenis_expressions(points,sets)
                points[point-1][i] += 15
                if points[point-1][i] == 45:
                    points[point-1][i] -= 5
                    if points[0][i] == 40 and points[1][i] == 40:
                        print_progress(points,abc)                      
                        while points[0][i] != 42 and points[1][i] != 42:
                            p = int(input("Who won the point: "))
                            print_progress(points,abc)
                            if p == 1:
                                points[p-1][0] += 1
                                tenis_expressions(points,sets)
                            elif p == 2:
                                points[p-1][0] += 1
                                print(f"{tenis_expressions(points,sets)} for {abc[p-1]}\n")
                            if points[0][0] == 42 or points[1][0] == 42:
                                points[p-1][1] += 1
                                points[0][i] = 0
                                points[1][i] = 0
                                break
                elif points[point-1][i] == 55:
                    points[point-1][i] += 5
                print_progress(points,abc)
                if points[point-1][i] == 60:
                    points[point-1][i+1] += 1
                    points[0][i] = 0
                    points[1][i] = 0
                    print_progress(points,abc)
                    if points[point-1][i+1] == 6:
                        points[point-1][i+2] += 1
                        points[0][i+1] = 0
                        points[1][i+1] = 0
                        print_progress(points,abc)
                        if points[0][2] == sets or points[1][2] == sets:
                            print(win(suma(points),abc))
                            break
            case 3:
                print(win(suma(points),abc))
                break
            case 4:
                print("Invalid, try again")
def print_progress(a,abc):
    #This function helps me show how the game is going as it is on the Tv
    print(f"{a[0]}: {abc[0]}")
    print(f"{a[1]}: {abc[1]}")

def names():
#It helps introduce identity to the user in the game
    name = []
    for i in range(2):
        names = input("Name of player: ")
        names = names.strip().title()
        name.append(names)
    return(name)

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

def abbreviations(name):
    a = []
    for i in name:
        parts = i.split()
        if len(parts) > 1:
            short = parts[0][0] + parts[1][0:2]
        else:
            short = i[:3]
        a.append(short.upper())
    return a

def tenis_expressions(a,b,n,sets):
    for i in range(len(a)):
        if a[i][0] == 0:
            print("Love\n")
            break
        elif a[0][0] == 40 and a[1][0] == 40:
            print("Deuce\n")
        elif a[i][0] == 41:
            print("Advantage")
        elif a[i][1] == 5:
            print("Game point\n")
        elif a[i][0] == 40 and a[i][1] == 5 and a[i][2] == sets - 1:
            print("Match point\n")

def main():
    #The function helps organise all of the other functions into one
    name = names()
    abc = abbreviations(name)
    print(abc[0], "vs" ,abc[1])
    while True:
        menu()
        option = int(input("Choose: "))
        match option:
            case 1:
                print(basketball(name))
            case 2:
                print(tennis(name))
            case 3:
                print(soccer(name))
            case 4:
                break
            case _:
                print("Invalid, try again")
main()
