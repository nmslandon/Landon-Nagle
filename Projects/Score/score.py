print('What is the home team?')
team1 = input()
print('What is the away team?')
team2 = input()
print('How many points did the home team score?')
score1 = input()
print('How many points did the away team score?')
score2 = input()
print(team1,'versus',team2)
print('Final score:' ,team1,'scored',score1,'points and' ,team2,'scored' ,score2, 'points')

if score1 > score2:
    print(team1,'wins!')
if score1 < score2:
    print(team2,'wins!')