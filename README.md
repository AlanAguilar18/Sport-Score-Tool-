# Sport-Score-Tool

Context:
Every sport keeps score in a different way. In soccer it is very simple: the team with more goals wins. Basketball gives a different number of points depending on the kind of shot, and it is played in four quarters. Tennis uses a structure of points, games and sets, with special rules like deuce and advantage.

Because of this, there is no single scoreboard that works for every sport. Someone has to learn a new set of rules for every sport they want to follow. This makes the problem interesting, because the process of scoring is always the same, but the rules change completely from sport to sport. As someone who plays different kinds of sports every day, I sometimes get confused by the specific rules of each one, so this program helps me every day.

This project solves that problem by having you pick a sport first and then loading a function that contains only the scoring rules of that sport. This way the same program can keep track of a match in any of its three sports (basketball, tennis and soccer) without you having to remember every rule yourself. The results are saved automatically, and you can read them or clear them directly from the main menu.

## Algorithm
1. You type the names of the two players or teams. If you leave a name empty, the program uses "Player 1" or "Player 2".
2. The program makes a short abbreviation for each name, like on a TV scoreboard, and shows the match for example ALA vs MAN (Alan/Manuel).
3. The main menu appears: 1. Basketball, 2. Tennis, 3. Soccer, 4. End, 5. Read or Clear.
4. When you pick a sport, the program loads the function with the scoring rules of that sport, and the score starts at zero for both sides.
5. You wait for a scoring action to happen and record who scored. You can choose "End" at any moment to finish the game early.
6. In basketball you also record the kind of action: a shot from the paint is worth 2, a three-pointer is worth 3, and a foul gives two free throws worth 1 each if they go in. The game is played in 4 quarters.
7. In tennis you first choose a match of 3 or 5 sets. Points move in order 0, 15, 30, 40, game, with deuce and advantage if both players reach 40. 6 games make a set, and the program shows expressions like Love, Deuce, Advantage and Game point.
8. In soccer every goal is worth 1, and the game is played in two halves.
9. After every action the program shows the scoreboard.
10. In basketball and soccer the game ends after the last quarter or half. In tennis it ends when a player wins enough sets (2 of 3, or 3 of 5).
11. The program compares the final score. The side with more points wins, and if both have the same points it is a tie.
12. The winner and the loser are shown in big colored letters.
13. The program saves automatically if each player won (W) or lost (L) in the file results.txt. Ties are not saved.
14. The program goes back to the main menu, so you can track another match with the same players.
15.With option 5 you can read all the saved results or clear the file.
16. With option 4 the program ends.

## External-Libraries
The program uses two external libraries: 
Colorama: which adds colors to the text in the terminal.
Pyfiglet: which turns text into big letters. 
To install them, open a new cmd or terminal and run:

python -m pip install colorama
python -m pip install pyfiglet

If you have an error that the library is not found then check that VS Code is using the same Python interpreter where you installed it so use Ctrl + Shift + P then select "Python: Select Interpreter". After installing, you can also reload VS Code with Ctrl + Shift + P then search for "Developer: Reload Window".
