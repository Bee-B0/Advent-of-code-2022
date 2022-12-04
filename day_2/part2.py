suma=[]
rules={"A":"B","B":"C","C":"A"} #lose:win
ruleslose={"B":"A","C":"B","A":"C"} #win:rock


points={"A":1,"B":2,"C":3}
## A = rock
## B= paper
## C= scissors

## X=lose
## Y=  tie
## Z= win



file = open('game.txt', 'r')
game = []
for line in file:
    newLst = []
    for c in line:
        newLst.append(c)
    game.append(newLst)
#print(game)


for roundnum in range(len(game)): #len(game)
  opponent = game[roundnum][0]
  if game[roundnum][2] == "X":#lose
    mymove=ruleslose[opponent]
    suma.append(points[mymove])
    #print(roundnum, points[mymove])

  

    
  elif game[roundnum][2] == "Y": #tie
    mymove= opponent
    suma.append(points[mymove]+3)
    #print(roundnum, points[mymove]+3)

  else: #win Z
    mymove=rules[opponent]
    suma.append(points[mymove]+6)
    #print(roundnum, points[mymove]+6)

    
    
##right answer 10334


print(sum(suma))
