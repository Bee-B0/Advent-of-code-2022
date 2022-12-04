#Day 1 part 2 https://adventofcode.com/2022/day/1
with open("calories.txt", 'r') as f:
    cal = f.readlines()

  
lcl=[0,0,0] #largest calories list

tcl=[0] #temporary calories list


for i in cal:
  if i =="\n":
    lcl.append(sum(tcl))
    tcl.clear()
  else:
    tcl.append(int(i))

print(sum(lcl[-3:]))

