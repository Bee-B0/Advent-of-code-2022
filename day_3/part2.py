list=[]
dict1 = {**{chr(i+96):i for i in range(1,27)},**{chr(i+64):i+26 for i in range(1,27)}}
# ** unpacks dictionaries, used for merging dictionaries

stringlist=open("strings.txt").readlines() # a list


def getnum(string): #going to split the list in half and tell me the values( from the dictionary) of the common letter in the two halves
  n="" # this is where I will store the same letter
  string1=stringlist[i] 
  string2=stringlist[i+1]
  string3=stringlist[i+2]
  

  for char in string1:
    if char in string2:
      if char in string3: # could use and, but thought it was easier to read like this. 
        n+=char
        print("yay "+n)
        return dict1[n]



for i in range(0,300,3): # going to run get num for all of the strings. 
  list.append(getnum(stringlist[i]))

  
total = sum(list)
print(total) #final answer
