#Day 1 part 1 https://adventofcode.com/2022/day/1
with open("calories.txt", 'r') as f:
    cal = f.readlines()
## The list is split up into strings
#['7896\n','4992\n',etc]
#This creates a problem that they are not int
#but thanks to this the blank lines are not deleated and are instead just \n
  
lcl=[0] #largest calories list
tcl=[0] #temporary calories lsit


for i in range(len(cal)):
  if cal[i] != "\n": #checks if it isn't a blank space
    tcl.append(int(cal[i])) #  we have to turn that sting into an int so we can sum it later on.

  else: # the \n (blank line) denotes the end of one group and the start of the next. 
    if sum(tcl)>sum(lcl): # checking if this group's total was greater than the last groups total
      lcl=tcl # if it is then we need to make the largest one this one. 
    tcl=[] #empties the box for the next iteration. 
    
  Sum = sum(lcl)
print(Sum) 
