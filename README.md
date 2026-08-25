# Sport-Score-Tool-

Context:
Every sport keeps a form to score in different ways, in soccer is a very simple way as the team who wins is the one with more goals. Tennis uses a structure of points, games, and sets, with special rules like deuce and advantage. Volleyball uses rally scoring with a win by two rule and a different point target for the deciding set. American football awards different point values depending on how a team scores like touchdown, extra point, field goal, safety. Golf does not count who has more points, it counts strokes, and fewer is better.

Because of this, there is no single scoreboard that works for every sport. Someone has to learn a new set of rules for every sport they want to support, so this makes the problem more interesting as the process of scoring is always the same, but the rules change completely from sport to sport. This situation makes it frustrating as someone who plays different kind of sports every day sometimes I get confused by the specific rules of each sport so  this program will help me every day.

Algorithm:
1. You pick a sport, tennis, american football, soccer, basketball, volleyball, ping pong or golf
2. It gives you to register you or your team in the data base for future matches
3. The program loads the scoring rules that belong to that sport
4. The score starts at zero for both sides
5. You wait for a scoring action to happen during the match
6. You record what type of action it was
7. The program adds the value that action is worth
8. In tennis the points move in order 0, 15, 30, 45, game, with a deuce and advantage rule if both players reach 45
9. In american football a touchdown is worth 6, an extra point 1, a two-point conversion 2, a field goal 3, and a safety 2
10. In soccer a goal is worth 1
11. In basketball a shot is worth 2, or 3 if it’s from beyond the arc, and a free throw is worth 1
12. In volleyball and ping pong every rally won is worth 1 point
13. In golf instead of adding points, you record the number of strokes it took to finish the hole
14. In tennis, the one who wins is the player that won enough sets
15. In american football, basketball, soccer
16. In volleyball and ping pong a side reached the point target with a 2-point lead and won enough sets or games
17. In golf all the holes have been played
18. Then the program compares the final score, or in golf the total strokes
21. The winner is the side with more points, except in golf where it’s the side with fewer strokes
22. You’re asked if you want to track another match
23. If you do the the program goes back to picking a sport
24. The program register if you won or losed
