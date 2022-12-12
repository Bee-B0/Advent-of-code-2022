
file = open('todo.txt', 'r')
x=1
i=0 ##cycle

list=[]
checkpoint=[20,60,100,140,180,220,260]


def meter(i,x):
  if i in checkpoint:
    print(i,"*",x," = ",i*x)
    list.append(x*i)


#14860 is the correct answer.
    

for a in range(137):
  
  action = file.readline()

  i=i+1 # for both of them, nothing happens in the first cycle. 
  meter(i,x) 

  #since noop does nothing but increase a cycle, we don't have to code for it. 

  if action.startswith("addx"): # "during the second cycle x is still 1" means that the cycle gets increased and it is checked if the cycle is at a checkpoint before x is increased. (That was from the instructions given.)
    i=i+1
    meter(i,x)

    action=action.strip("addx ")
    action=action.strip("\n")
    
    x=x+int(action)


file.close()

print(sum(list))## the final total. 
