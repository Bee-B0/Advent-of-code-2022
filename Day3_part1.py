##https://adventofcode.com/2022/day/3
#part1

list=[]
dict1 = {**{chr(i+96):i for i in range(1,27)},**{chr(i+64):i+26 for i in range(1,27)}}

stringlist=open("strings.txt").readlines() # a list

def getnum(string): #going to split the list in half and tell me the values( from the dictionary) of the common letter in the two halves
  string1, string2 = string[:len(string)//2], string[len(string)//2:]
  n=""
  for char in string1:
    if char in string2 and char not in n:
      n+=char 
  
  #print(dict1[n])
  return dict1[n]

for i in range(len(stringlist)): # going to run get num for all of the strings. 
  list.append(getnum(stringlist[i]))

  
  Sum = sum(list)
print(Sum) #final answer
  

  
