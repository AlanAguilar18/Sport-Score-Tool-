"""
SPORT SCORER TOOL
Multi Sport Scorer
Author: Alan 
"""
"""
Context:
Every sport has a different form to score, so this program solves that by letting the user pick one sport of the options 
from the menu and loading a function with only that sport’s scoring rules, so it tracks the match correctly without 
the user having to remember them all. Also you can use the option 5 → read which will save the results and show the porcentage of victories in all the sports.

External library:
In my code I used the external library colorama which is really easy to install, you need to open cmd/terminal where you need to copy and paste "pip install colorama",
just a little tip is that I had some problems with it at first as I was not using the proper python intepreter (check that for no futher problems). Well I also 
added pyfiglet that is really similar to colorama where you paste "python -m pip install pyfiglet" on the terminal and reload the page with "Developer: Reload Window".
"""
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import pyfiglet
init(autoreset=True)

def save(name, sum):
    #Save the result (W or L) of each player in the results file.
    try:
        with open("results.txt", "a") as results:
            results.write(f"{name[0]}={sum[0]}\n")
            results.write(f"{name[1]}={sum[1]}\n")
    except FileExistsError:
        print("The file does not exist")

def read():
    #It prints the results saved in the results file given by the save function.
    try:
        with open("results.txt", "r") as results_file:
            for i in results_file:
                a = i.strip()
                p = a.split("=")
                name = p[0]
                result = p[1]
                print(f"{name}: {result}")
    except FileNotFoundError:
        print("The file does not exist")

def menu():
    #Prints the main menu with the available options of the different sports.
    print("Choose an option: ")
    print("1. Basketball")
    print("2. Tennis")
    print("3. Soccer")
    print("4. End")
    print("5. Read the last matches")

def ask_number(message):
    #It helps validating the inputs so it only gives me a number.
    while True:
        try:
            return(int(input(message)))
        except ValueError:
            print("Invalid type a number")

def options(name):
    #This one prints the options to choose a player/team or end the game.
    print("Choose an option: ")
    print(f"1 → {name[0]}")
    print(f"2 → {name[1]}")
    print("3 → End")

def options_basketball():
    #It presents the different kinds of basketball actions and their respective points.
    print("Choose an option: ")
    print("1. From the paint → 2 points")
    print("2. From the three point line → 3 points")
    print("3. Foul → 1 or 2 points")

def sum(a):
    #Thsi function returns a list with the sum of the matrix.
    Sum = []
    for i in a:
        total = 0
        for j in i:
            total += j
        Sum.append(total)
    return(Sum)

def basketball(name):
    #Keep the score of a basketball game quarter by quarter played by 2 teams.
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
                    print_progress(sum(game),abc)
                    return win(sum(game),name)
                case 4:
                    i += 1
                    if i == 4:
                        print(" Q1|Q2|Q3|Q4")
                        print_progress(game,abc)
                        print_progress(sum(game),abc)
                        return win(sum(game),name)
                case _:
                    print("Invalid, try again")

def soccer(name):
    #Keep the score of a soccer game half by half played by 2 teams.
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
                    print_progress(sum(goals),abc)
                    return(win(sum(goals),name))
                case 4:
                    i += 1
                    if i == 2:
                        print_progress(sum(goals),abc)
                        return(win(sum(goals),name))
                case _:
                    print("Invalid")
            print_progress(goals,abc)

def tennis(name):
    #Keep the score of a tennis match until a player wins it by the sets the player decides.
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
                            if p == 1:
                                points[p-1][0] += 1
                                print(tenis_expressions(points,sets)," for ",abc[p-1],"\n")
                            elif p == 2:
                                points[p-1][0] += 1
                                print(tenis_expressions(points,sets)," for ",abc[p-1],"\n")
                            if points[0][0] == 41 and points[1][0] == 41:
                                points[0][0] = 40
                                points[1][0] = 40
                                tenis_expressions(points,sets)
                            if points[0][0] == 42 or points[1][0] == 42:
                                points[p-1][1] += 1
                                points[0][i] = 0
                                points[1][i] = 0
                                break
                elif points[point-1][i] == 55:
                    points[point-1][i] += 5
                if points[point-1][i] == 60:
                    points[point-1][i+1] += 1
                    points[0][i] = 0
                    points[1][i] = 0
                    if points[point-1][i+1] == 6:
                        points[point-1][i+2] += 1
                        points[0][i+1] = 0
                        points[1][i+1] = 0
                        if points[0][2] == sets or points[1][2] == sets:
                            print(win(sum(points),name))
                            break
            case 3:
                print(win(sum(points),name))
                break
            case 4:
                print("Invalid, try again")
        print_progress(points,abc)

def print_progress(a,abc):
    #This function helps me show how the game is going as it is on the Tv
    print(f"{a[0]}: {abc[0]}")
    print(f"{a[1]}: {abc[1]}\n")

def names():
    #Ask for the names of the two players/teams and return them in a list.
    name = []
    for i in range(2):
        names = input("Name of player: ")
        names = names.strip().title()
        name.append(names)
    return(name)

def win(a,name):
    #This function helps me simplifying in all the sports on the program to determine who is the winner
    w = ["W","L"]
    if a[0] > a[1]:
        save(name, w)
        return(pyfiglet.figlet_format(f"{name[0]} won\n{name[1]} lost"))
    elif a[1] > a[0]:
        save(name, w[::-1])
        return(pyfiglet.figlet_format(f"{name[1]} won\n{name[0]} lost"))
    elif a[0] == a[1]:
        return(pyfiglet.figlet_format("TIE"))
    else:
        return("DNP")

def abbreviations(name):
    #In many sports mainly in soccer the use abbreviations instead of the complete name of the team as the scores boards are tiny in comparison to the ones in basketball
    a = []
    for i in name:
        parts = i.split()
        if len(parts) > 1:
            short = parts[0][0] + parts[1][0:2]
        else:
            short = i[:3]
        a.append(short.upper())
    return a

def tenis_expressions(a,sets):
    #In tenis we have different expressions depending the score so this helps me saving them an using them on the tenis game
    for i in range(len(a)):
        if a[0][0] == 0 and a[1][0] == 0:
            print(Fore.GREEN + "Love\n")
            break
        elif a[0][0] == 40 and a[1][0] == 40:
            print(Fore.YELLOW + "Deuce\n")
            break
        elif a[i][0] == 41:
            return("Advantage")
        elif a[i][1] == 5:
            print(Fore.RED + "Game point\n")
        elif a[i][0] == 40 and a[i][1] == 5 and a[i][2] == sets - 2:
            print(Fore.RED + "Match point\n")

def main():
    #Ask for the players and show the main menu that organises all the games until the user ends it.
    name = names()
    abc = abbreviations(name)
    print(Style.BRIGHT + abc[0], "vs" ,abc[1] + Style.RESET_ALL)
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
            case 5:
                read()
            case _:
                print("Invalid, try again")
main()
