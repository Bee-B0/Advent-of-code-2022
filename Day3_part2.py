list=[]
dict1 = {**{chr(i+96):i for i in range(1,27)},**{chr(i+64):i+26 for i in range(1,27)}}


stringlist=open("strings.txt").readlines() # a list
print(stringlist)
def getnum(string): #going to split the list in half and tell me the values( from the dictionary) of the common letter in the two halves
  n=""
  string1=stringlist[i]
  print(string1)
  string2=stringlist[i+1]
  print(string2)
  string3=stringlist[i+2]
  print(string3)

  for char in string1:
    #print(char)
    if char in string2:
      if char in string3:
        n+=char
        print("yay "+n)
        return dict1[n]



for i in range(0,300,3): # going to run get num for all of the strings. 
  list.append(getnum(stringlist[i]))

  
Sum = sum(list)
print(Sum) #final answer
