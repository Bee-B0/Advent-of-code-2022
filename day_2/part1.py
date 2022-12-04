suma=[]
rules={"A":"Y","B":"Z","C":"X"}
same= {"A":"X","B":"Y","C":"Z"}
points={"X":1,"Y":2,"Z":3}
win= 6
## A = rock
## B= paper
## C= scissors

## X=rock
## Y=  paper
## Z= scissors



file = open('game.txt', 'r')
game = []
for line in file:
    newLst = []
    for c in line:
        newLst.append(c)
    game.append(newLst)
#print(lst)



for roundnum in range(len(game)):
  #print(game[roundnum])
  if game[roundnum][2] == rules[game[roundnum][0]]:
    suma.append(win)
    suma.append(points[game[roundnum][2]])


    
  elif game[roundnum][2] == same[game[roundnum][0]]:
    suma.append(win/2)
    suma.append(points[game[roundnum][2]])

  else:
    suma.append(points[game[roundnum][2]])

print(sum(suma))

    
