"""
SPORT SCORER TOOL
Multi Sport Scorer
Author: Alan Aguilar

Context:
Every sport has a different form to score, so this program
solves that by letting the user pick one sport of the options
from the menu and loading a function with only that sport’s
scoring rules, so it tracks the match correctly without
the user having to remember them all. Also you can use the
option 5 → read/clear where the results are saved automatically
and it can also clear the document.
"""
from colorama import Fore, Style, init
import pyfiglet
init(autoreset=True)


def save(name, sum):
    # Save the result (W or L) of each player in the results file.
    try:
        with open("results.txt", "a") as results:
            results.write(f"{name[0]}={sum[0]}\n")
            results.write(f"{name[1]}={sum[1]}\n")
    except FileExistsError:
        print("The file does not exist")


def read_or_clear():
    """
    Inputs:
    Option chosen: 1 to read or 2 to clear, typed by the user.
    Results file: results.txt, with the games saved before.
    Outputs:
    Results on screen: each saved line as "name: result".
    Empty file: results.txt erased and the message "File cleared".
    Warning: the rpogram prints "The file doesn't exist yet" if there is no 
    file to read.
    Process:
    1. Shows the two options and asks for one.
    2. To read: opens the file, goes line by line, separates the name from the
    result at the "=" and prints them.
    3. To clear: opens the file in write mode, which leaves it empty.
    4. If the file doesn't exist when reading, it shows the warning instead
       of crashing.
"""
    print("1. Read")
    print("2. Clear")
    option = ask_number("Choose an option: ")
    match option:
        case 1:
            try:
                with open("results.txt") as results_file:
                    for i in results_file:
                        parts = i.strip()
                        parts = parts.split("=")
                        name, result = parts
                        print(f"{name}: {result}")
            except FileNotFoundError:
                print("The file doesn't exist yet")
        case 2:
            print("File cleared\n")
            with open("results.txt", "w"):
                pass
        case _:
            print("Invalid")
    print()


def ask_number(message):
    # It helps validating the inputs so it only gives me a number.
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid type a number")


def options_basketball():
    # Show the kinds of basketball actions and their points.
    print("Choose an option: ")
    print("1. From the paint → 2 points")
    print("2. From the three point line → 3 points")
    print("3. Foul → 1 or 2 points\n")


def sum(matrix):
    # This function returns a list with the sum of the matrix.
    sum = []
    for i in matrix:
        total = 0
        for j in i:
            total += j
        sum.append(total)
    return sum


def show_matrix(score, short_abbreviation):
    # This function helps me show how the game is going as it is on the Tv
    for i in range(len(score)):
        for j in range(len(score[i])):
            print(f"{score[i][j]}", end=" | ")
        print(short_abbreviation[i])


def show_total(total, short_abbreviation):
    # Print the total points of each player with its abbreviation.
    for i in range(len(total)):
        print(f"Total: {total[i]} | {short_abbreviation[i]}")


def basketball(name, short_abbreviation):
    """
    Inputs:
    Names and abbreviations of both teams.
    Who scored 1 or 2, or 3 to end and 4 for the next quarter.
    Kind of shot between paint, three-pointer or foul.
    Free throws in or out, for each of the two shots of a foul.
    Outputs:
    Scoreboard on screen points of each team per quarter from
    Q1 to Q4, after every play. Final totals and winner shown
    when the game ends.
    Process:
    1. Starts a scoreboard with 4 quarters at 0 for each team.
    2. Asks who scored and what kind of shot it was, and adds 2,
       3, or 1 per free throw that goes in.
    3. Option 4 moves to the next quarter and after the 4th
       quarter the game ends.
    4. Option 3 ends the game at any moment of the match.
    5. At the end, it shows the totals and sends them to win to
       know who won.
    """
    score = [
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]
    i = 0
    while i < 4:
        while True:
            options(name)
            print("4 → Next quarter\n")
            print("Q1| Q2| Q3| Q4|")
            show_matrix(score, short_abbreviation)
            point = ask_number("¿Who did the point? ")
            match point:
                case 1 | 2:
                    options_basketball()
                    basket = ask_number("¿What kind of action was it? ")
                    match basket:
                        case 1:
                            score[point-1][i] += 2
                        case 2:
                            score[point-1][i] += 3
                        case 3:
                            first_foul = ask_number(
                                "First shoot\n1 → in\n2 → out\nChoose: ")
                            match first_foul:
                                case 1:
                                    score[point-1][i] += 1
                                case 2:
                                    print("Next time")
                                case _:
                                    print("Invalid")
                            second_foul = ask_number(
                                "Second shoot\n1 → in\n2 → out\nChoose: ")
                            match second_foul:
                                case 1:
                                    score[point-1][i] += 1
                                case 2:
                                    print("Really???")
                                case _:
                                    print("Invalid")
                        case _:
                            print("Invalid")
                case 3:
                    print("Q1| Q2| Q3| Q4|")
                    show_matrix(score, short_abbreviation)
                    show_total(sum(score), short_abbreviation)
                    return win(sum(score), name)
                case 4:
                    i += 1
                    if i == 4:
                        print("Q1| Q2| Q3| Q4|")
                        show_matrix(score, short_abbreviation)
                        show_total(sum(score), short_abbreviation)
                        return win(sum(score), name)
                case _:
                    print("Invalid, try again")


def soccer(name, short_abbreviation):
    """
    Inputs:
    Names and abbreviations of both teams.
    Who scored 1 or 2, or 3 to end and 4
    for half time.
    Outputs:
    Scoreboard on screen goals of each team
    in the first and second half, after every goal.
    Final totals and winner shown when the game ends.
    Process:
    1. Starts a scoreboard with 2 halves at 0 for each team.
    2. Every goal adds 1 to that team in the current half.
    3. Option 4 goes to the second half and after the second
       time the game ends.
    4. Option 3 ends the game at any moment.
    5. At the end, it shows the totals and sends them to win.
    """
    score = [
        [0, 0],
        [0, 0]
        ]
    i = 0
    while i < 2:
        while True:
            options(name)
            print("4 → Half time\n")
            who = ask_number("Which team scored: ")
            match who:
                case 1 | 2:
                    score[who-1][i] += 1
                case 3:
                    show_total(sum(score), short_abbreviation)
                    return win(sum(score), name)
                case 4:
                    i += 1
                    if i == 2:
                        show_total(sum(score), short_abbreviation)
                        return win(sum(score), name)
                case _:
                    print("Invalid")
            show_matrix(score, short_abbreviation)


def tenis_expressions(points, sets):
    # Print the tennis expressions that match the score.
    for i in range(len(points)):
        if points[0][0] == 0 and points[1][0] == 0:
            print(Fore.GREEN + "Love")
            break
        elif points[0][0] == 40 and points[1][0] == 40:
            print(Fore.YELLOW + "Deuce")
            break
        elif points[i][0] == 41:
            return Fore.LIGHTRED_EX + "Advantage"
        elif points[i][1] == 5 and points[i][0] == 40:
            print(Fore.RED + "Game point")
        elif (points[i][0] == 40 and points[i][1] == 5
              and points[i][2] == sets - 2):
            print(Fore.RED + "Match point\n")


def tennis(name, short_abbreviation):
    """
    Inputs:
    Names and abbreviations of both players.
    Length of the match 3 or 5 sets.
    Who won each point 1 or 2, or 3 to end.
    Outputs:
    Scoreboard on screen points | games | sets
    of each player, after every point. Tennis
    expressions like Love, Deuce, Advantage, Game point.
    Winner shown when someone gets the sets needed.
    Process:
    1. Asks for 3 or 5 sets and works out how many are
       needed to win (2 or 3).
    2. Every point goes 0 → 15 → 30 → 40 → game.
    3. If both players reach 40, it enters deuce there
       the player needs an advantage and then one more point
       to win the game.
    4. 6 games make a set, and the games go back to 0.
    5. When a player reaches the sets needed, it calls win.
    """
    score = [[0, 0, 0],
             [0, 0, 0]
             ]
    while True:
        sets = ask_number("Choose between a game of 3 or 5 sets: ")
        if sets != 3 and sets != 5:
            print("Try again")
        else:
            break
    if sets == 3:
        sets = 2
    elif sets == 5:
        sets = 3
    i = 0
    while score[0][2] < sets and score[1][2] < sets:
        options(name)
        point = ask_number("Who won the point: ")
        match point:
            case 1 | 2:
                tenis_expressions(score, sets)
                score[point-1][i] += 15
                if score[point-1][i] == 45:
                    score[point-1][i] -= 5
                    if score[0][i] == 40 and score[1][i] == 40:
                        tenis_expressions(score, sets)
                        show_matrix(score, short_abbreviation)
                        while score[0][i] != 42 and score[1][i] != 42:
                            action = ask_number("Who won the point: ")
                            if action == 1:
                                score[action-1][0] += 1
                                print(tenis_expressions(score, sets), " for ",
                                      short_abbreviation[action-1], "\n")
                            elif action == 2:
                                score[action-1][0] += 1
                                print(tenis_expressions(score, sets), " for ",
                                      short_abbreviation[action-1], "\n")
                            if score[0][0] == 41 and score[1][0] == 41:
                                score[0][0] = 40
                                score[1][0] = 40
                                tenis_expressions(score, sets)
                            if score[0][0] == 42 or score[1][0] == 42:
                                score[action-1][1] += 1
                                score[0][i] = 0
                                score[1][i] = 0
                                break
                elif score[point-1][i] == 55:
                    score[point-1][i] += 5
                if score[point-1][i] == 60:
                    score[point-1][i+1] += 1
                    score[0][i] = 0
                    score[1][i] = 0
                    if score[point-1][i+1] == 6:
                        score[point-1][i+2] += 1
                        score[0][i+1] = 0
                        score[1][i+1] = 0
                        if score[0][2] == sets or score[1][2] == sets:
                            return win(sum(score), name)
            case 3:
                return win(sum(score), name)
            case 4:
                print("Invalid, try again")
        show_matrix(score, short_abbreviation)
        print()


def win(sum_per_player, name):
    """
    Inputs:
    Totals: the final points of each player or team.
    List of names: the two players or teams.
    Outputs:
    Big text on screen: "won" with the winner's name in yellow and "lost"
    with the loser's name in red, or "TIE" in cyan.
    Saved result: W and L written in results.txt.
    Process:
    1. Compares the two totals.
    2. If the first one is bigger, player 1 wins: saves W and L and builds
    the big text.
    3. If the second one is bigger, player 2 wins: saves the results in the
    opposite order like L and W.
    4. If they are equal, it's a tie and nothing is saved.
    """
    results = ["W", "L"]
    if sum_per_player[0] > sum_per_player[1]:
        save(name, results)
        return (Fore.LIGHTYELLOW_EX
                + pyfiglet.figlet_format(f"{name[0]}    won\n")
                + (Fore.LIGHTRED_EX
                   + pyfiglet.figlet_format(f"{name[1]}    lost")))
    elif sum_per_player[1] > sum_per_player[0]:
        save(name, results[::-1])
        return (Fore.LIGHTYELLOW_EX
                + pyfiglet.figlet_format(f"{name[1]}    won\n")
                + (Fore.LIGHTRED_EX
                   + pyfiglet.figlet_format(f"{name[0]}    lost")))
    elif sum_per_player[0] == sum_per_player[1]:
        return Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("TIE")


def welcome(option):
    # Print the name of the chosen sport in its color.
    match option:
        case 1:
            print(Fore.RED + "Basketball")
        case 2:
            print(Fore.GREEN + "Tennis")
        case 3:
            print(Fore.WHITE + "Soccer")


def menu():
    # Print the main menu with the sports and the results option.
    print("Choose an option: ")
    print("1. Basketball")
    print("2. Tennis")
    print("3. Soccer")
    print("4. End")
    print("5. Read or Clear")


def names():
    # Ask for the names of the two players/teams and return them in a list.
    name = []
    for i in range(2):
                names = input("Name of player: ").strip()
        if len(names) == 0:
            name.append("Player " + str(i+1))
        else:
            name.append(names.title())
            name.append(names)
    return name


def options(name):
    # This one prints the options to choose a player/team or end the game.
    print("Choose an option: ")
    print(f"1 → {name[0]}")
    print(f"2 → {name[1]}")
    print("3 → End")


def abbreviations(name):
    # Abbreviations instead of the complete name.
    abbreviation = []
    for words in name:
        parts = words.split()
        if len(parts) > 1:
            short_form = parts[0][0] + parts[1][0:2]
        else:
            short_form = parts[0][:3]
        abbreviation.append(short_form.upper())
    return abbreviation


def main():
    # Ask for the players and show the menu until the user ends it.
    name = names()
    short_abbreviation = abbreviations(name)
    print(Style.BRIGHT + f"{short_abbreviation[0]} vs "
          f"{short_abbreviation[1]}" + Style.RESET_ALL + "\n")
    while True:
        menu()
        option = ask_number("Choose: ")
        print()
        try:
            match option:
                case 1:
                    welcome(option)
                    print(basketball(name, short_abbreviation))
                case 2:
                    welcome(option)
                    print(tennis(name, short_abbreviation))
                case 3:
                    welcome(option)
                    print(soccer(name, short_abbreviation))
                case 4:
                    break
                case 5:
                    read_or_clear()
                case _:
                    print("Invalid, try again")
        except ValueError:
            print("Invalid please try again")


main()
