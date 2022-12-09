stack1=["R","S","L","F","Q"]
stack2=["N","Z","Q","G","P","T"]
stack3=["S","M","Q","B"]
stack4=["T","G","Z","J","H","C","B","Q"]
stack5=["P","H","M","B","N","F","S"]
stack6=["P","C","Q","N","S","L","V","G"]
stack7=["W","C","F"]
stack8=["Q","H","G","Z","W","V","P","M"]
stack9=["G","Z","D","L","C","N","R"]
allstacks=[stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]


current=[]

txt= open('steps.txt').readlines()
#print(txt)
for line in txt:

  # the set up so that the instructions can be interpreted by the computer. 
  current=[]
  line = line.replace('\n','')
  line= line.replace("move","")
  line= line.replace(" to "," from ")
  current=line.split(" from ")
  print(current)
  takefromlist=(allstacks[int(current[1])-1])
  putherelist=(allstacks[int(current[2])-1])
  
  print(takefromlist)

  numcrates= int(current[0]) #how many we are moving
  #----------------------------
  #below is the part of the code that moves things. 
  temp=[]#temporary storage that will reset every time it is a new instruction line. 
  
  
  for i in range(numcrates): ## how many we are moving
    x=len(takefromlist)-numcrates+i   
    temp.append(takefromlist[x])
    takefromlist.pop(x)
    putherelist.append(temp[len(temp)-1]) 

print("*"*20) # a nice little divider. 

#prints the code. There is probably a better way to do this. . .
print(stack1[-1],stack2[-1],stack3[-1],stack4[-1],stack5[-1],stack6[-1],stack7[-1],stack8[-1],stack9[-1])


