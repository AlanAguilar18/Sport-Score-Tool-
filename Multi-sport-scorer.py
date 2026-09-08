def menu():
  """It helps the user see the options it has to choose between"""
    print("Choose an option: ")
    print("1. Basketball")
    print("2. Tennis")
    print("3. Soccer")
    
def basketball(player_1,player_2):
  """It calculates the score of every shot made on court between 2 teams/individuals and can determine who wins or loses"""
    match = 0
    while match == 0:
        point = input("Which won the point(player1,player2,end): ")
        if(point == "player1"):
            canasta1 = input("¿What kind of action was it?(paint/three point/foul): ")
            if(canasta1 == "paint"):
                player_1 = player_1 + 2
                print(player_1,"/",player_2)
            elif(canasta1 == "three point"):
                player_1 = player_1 + 3
                print(player_1,"/",player_2)
            elif(canasta1 == "foul"):
                foul = input("First shoot (yes/no): ")
                if foul == "yes":
                    player_1 = player_1 + 1
                    foul2 = input("Second shoot(yes/no): ")
                    if foul2 == "yes":
                        player_1 = player_1 + 1
                    elif foul2 == "no":
                        print("Really???")
                elif foul == "no":
                    print("Good luck next time")
                    foul5 = input("Second shoot(yes/no): ")
                    if(foul5 == "yes"):
                        player_2 = player_2 + 1
                        print(player_1,"/",player_2)
                    elif(foul3 == "no"):
                        print("Really???")
        elif(point == "player2"):
            canasta2 = input("¿What kind of action was it?(from the paint, three point or from a foul): ")
            if(canasta2 == "paint"):
                player_2 = player_2 + 2
                print(player_1,"/",player_2)
            elif(canasta2 == "three point"):
                player_2 = player_2 + 3
                print(player_1,"/",player_2)
            elif(canasta2 == "foul"):
                foul1 = input("First shoot (yes/no): ")
                if(foul1 == "yes"):
                    player_2 = player_2 + 1
                    print(player_1,"/",player_2)
                    foul3 = input("Second shoot(yes/no): ")
                    if(foul3 == "yes"):
                        player_2 = player_2 + 1
                        print(player_1,"/",player_2)
                    elif(foul3 == "no"):
                        print("Really???")
                elif(foul == "no"):
                    print("Good luck next time")
                    foul4 = input("Second shoot(yes/no): ")
                    if(foul4 == "yes"):
                        player_2 = player_2 + 1
                        print(player_1,"/",player_2)
                    elif(foul4 == "no"):
                        print("Really???")
        elif(point == "end"):
            match = 1
            print(player_1,"/",player_2)
        else:
            print("Invalid, try again")
    if player_1 > player_2:
        print("Player 1 won and Player 2 lost")
    elif player_2 > player_1:
        print("Player 2 won and Player 1 lost")
    else:
        print("DNP")
    return(player_1,player_2)

def soccer(team_a,team_b):}
  """It calculates the score of every goal between 2 teams and can determine who wins or loses"""
    match = 0
    while match == 0:
        goal = input("Which team scored(a,b,end): ")
        if(goal == "a"):
            team_a = team_a+1
        elif(goal == "b"):
            team_b = team_b+1
        elif(goal == "end"):
            match = 1
        else:
            print("Invalid")
    if team_a > team_b:
        print("team_a won and team_b lost")
    elif team_b > team_a:
        print("team_b won and team_a lost")
    else:
        print("Tie")
    return(team_a,team_b)

def tennis(player1,player2):
  """It calculates the score of every point made, the program also can dertermine when it is a game and a set between 2 individuals and can determine who wins or loses"""
    match = 0
    points = 0
    points1 = 0
    games = 0
    games1 = 0
    sets = int(input("Choose between a game of 3 or 5 sets: "))
    sets1 = 0
    sets2 = 0
    while match == 0:
        point = input("Which won the point(a,b,end): ")
        if(point == "a"):
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
        elif(point == "b"):
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
        elif(point == "end"):
            match = 1
        else:
            print("Invalid, try again")
    if player1 > player2:
        print("Player 1 won and Player 2 lost")
    elif player2 > player1:
        print("Player 2 won and Player 1 lost")
    else:
        print("DNP")
    return(player1,player2)

def main():
  """The function helps organise all of the other functions into one"""
    menu()
    option = int(input())
    if(option == 1):
        player_1 = 0
        player_2 = 0
        print(basketball(player_1,player_2))
    elif(option == 2):
        player1 = 0
        player2 = 0
        print(tennis(player1,player2))
    elif(option == 3):
        team_a = 0
        team_b = 0
        print(soccer(team_a,team_b))
    else:
        print("Can't identify that game")
    return
main()
