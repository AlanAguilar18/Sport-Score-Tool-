# Sport-Score-Tool-

Context:
Every sport keeps a form to score in different ways, in soccer is a very simple way as the team who wins is the one with more goals. Tennis uses a structure of points, games, and sets, with special rules like deuce and advantage. Volleyball uses rally scoring with a win by two rule and a different point target for the deciding set. American football awards different point values depending on how a team scores like touchdown, extra point, field goal, safety. Golf does not count who has more points, it counts strokes, and fewer is better.

Because of this, there is no single scoreboard that works for every sport. Someone has to learn a new set of rules for every sport they want to support, so this makes the problem more interesting as the process of scoring is always the same, but the rules change completely from sport to sport. This situation makes it frustrating as someone who plays different kind of sports every day sometimes I get confused by the specific rules of each sport so  this program will help me every day.

This project aims to solve the problem that there is no single set of rules that works for every sport at scoring, so my program solves this by having you pick a sport first, then loading a function that contains only the scoring rules that belong to that sport, so the same program can correctly keep track of a match no matter which of the seven sports (tennis, american football, soccer, basketball, volleyball, ping pong and golf) you are playing, without you having to remember every of the sport rules yourself.

## Algorithm
1. You pick a sport, tennis, american football, soccer, basketball, volleyball, ping pong or golf
2. It gives you to register you or your team in the data base for future matches
3. The program loads the scoring rules that belong to that sport
4. It can also count the fouls during the game such as a yellow card in soccer
5. The score starts at zero for both sides
6. You wait for a scoring action to happen during the match
7. You record what type of action it was
8. The program adds the value that action is worth
9. In tennis the points move in order 0, 15, 30, 45, game, with a deuce and advantage rule if both players reach 45
10. In american football a touchdown is worth 6, an extra point 1, a two-point conversion 2, a field goal 3, and a safety 2
11. In soccer a goal is worth 1
12. In basketball a shot is worth 2, or 3 if it’s from beyond the arc, and a free throw is worth 1
13. In volleyball and ping pong every rally won is worth 1 point
14. In golf instead of adding points, you record the number of strokes it took to finish the hole
15. In tennis, the one who wins is the player that won enough sets
16. In american football, basketball, soccer the one who wins is who has the most points
17. In volleyball and ping pong a side reached the point target with a 2-point lead and won enough sets or games
18. In golf all the holes have been played
19. Then the program compares the final score, or in golf the total strokes
20. IF they have the same number of points it’s called a tie 
21. The winner is the side with more points, except in golf where it’s the side with fewer strokes
22. You’re asked if you want to track another match
23. If you do the the program goes back to picking a sport
24. The program register if you won or losed
