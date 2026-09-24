"""It helps the user see the options it has to choose between"""
def menu():
    print("Choose an option: ")
    print("1. Basketball")
    print("2. Tennis")
    print("3. Soccer")

"""The function shows a menu that helps the user choose an option of the three"""
def options():
    print("Choose an option: ")
    print("1 → Player 1")
    print("2 → Player 2")
    print("3 → End")

"""It helps choosing the type of action it was on the game"""
def options_basketball():
    print("Choose an option: ")
    print("1. From the paint → 2 points")
    print("2. From the three point line → 3 points")
    print("3. Foul → 1 or 2 points")

"""It calculates the score of every shot made on court between 2 teams/individuals and can determine who wins or loses"""
def basketball(player_1,player_2):
    match = 0
    while match == 0:
        options()
        point = int(input("¿Who won the point? "))
        match point:
            case 1:
                options_basketball()
                canasta1 = int(input("¿What kind of action was it? "))
                match canasta1:
                    case 1:
                        player_1 += 2
                    case 2:
                        player_1 += 3
                    case 3:
                        foul = input("First shoot (yes/no): ")
                        if foul == "yes":
                            player_1 += 1
                        elif foul == "no":
                            print("Next time")
                        else:
                            print("Invalid")
                        foul2 = input("Second shoot(yes/no): ")
                        if foul2 == "yes":
                            player_1 += 1
                        elif foul2 == "no":
                            print("Really???")
                        else:
                            print("Invalid")
                    case _:
                        print("Invalid")
                print(player_1,"/",player_2)
            case 2:
                options_basketball()
                canasta2 = int(input("¿What kind of action was it? "))
                match canasta2:
                    case 1:
                        player_2 += 2
                        print(player_1,"/",player_2)
                    case 2:
                        player_2 += 3
                        print(player_1,"/",player_2)
                    case 3:
                        foul1 = int(input("First shoot: "))
                        match foul1:
                            case 1:
                                player_2 = player_2 + 1
                                print(player_1,"/",player_2)
                            case 2:
                                print("Good luck next time")
                        foul3 = input("Second shoot(yes/no): ")
                        if(foul3 == "yes"):
                            player_2 = player_2 + 1
                            print(player_1,"/",player_2)
                        elif(foul3 == "no"):
                            print("Really???")
                        else:
                            print("Invalid")
                    case _:
                        print("Invalid, try again")
            case 3:
                match = 1
                print(player_1,"/",player_2)
            case _:
                print("Invalid, try again")
    return(win(player_1,player_2))

"""It calculates the score of every goal between 2 teams and can determine who wins or loses"""
def soccer(team_a,team_b):
    match = 0
    while match == 0:
        options()
        goal = int(input("Which team scored: "))
        match goal:
            case 1:
                team_a += team_a+1
            case 2:
                team_b = team_b+1
            case 3:
                match = 1
            case _:
                print("Invalid")
        print(team_a,"/",team_b)
    return(win(team_a,team_b))

"""It calculates the score of every point made, the program also can dertermine when it is a game and a set between 2 individuals and can determine who wins or loses"""
def tennis(player1,player2):
    match = 0
    points = 0
    points1 = 0
    games = 0
    games1 = 0
    sets = int(input("Choose between a game of 3 or 5 sets: "))
    sets1 = 0
    sets2 = 0
    while match == 0:
        options()
        point = int(input("Which won the point: "))
        match point:
            case 1:
                points = points+15
                print(points,"/",points1)
                if points == 60:
                    games = games + 1
                    points = 0
                    points1 = 0
                    print(games,"/",games1)
                    if games == 6:
                        sets1 = sets1 + 1
                        games = 0
                        print(sets1,"/",sets2)
                        if sets1 == sets:
                            player = 1
                            match = 1
            case 2:
                points1 = points1+15
                print(points,"/",points1)
                if points1 == 60:
                    games1 = games1 + 1
                    print(games,"/",games1)
                    points1 = 0
                    points = 0
                    if games == 6:
                        sets2 = sets2 + 1
                        games = 0
                        print(sets1,"/",sets2)
                        if sets2 == sets:
                            player2 = 1
                            match = 1
            case 3:
                match = 1
            case 4:
                print("Invalid, try again")
    return(win(player1,player2))

"""This function helps me simplifying in all the sports on the program to determine who is the winner"""
def win(a,b):
    if a > b:
        return("Player 1 won and Player 2 lost")
    elif b > a:
        return("Player 2 won and Player 1 lost")
    elif a == b:
        return("TIE")
    else:
        return("DNP")

"""The function helps organise all of the other functions into one"""
def main():
    menu()
    option = int(input("Choose: "))
    match option:
        case 1:
            player_1 = 0
            player_2 = 0
            print(basketball(player_1,player_2))
        case 2:
            player1 = 0
            player2 = 0
            print(tennis(player1,player2))
        case 3:
            team_a = 0
            team_b = 0
            print(soccer(team_a,team_b))
        case _:
            print("Invalid, try again")
main()
