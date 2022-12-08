total=0

txt= open('jobs.txt').readlines()
#print(txt)
for line in txt:
  line = line.replace('\n','')
  pair= line.split(",")
  #print(pair)
  a=pair[0].split("-")
  #print(a)
  b=pair[1].split("-")
  #print(b)

  ## -1 so that the boundrys include the numbers.
  if (int(a[0])-1<=int(b[0])-1 and int(b[1])+1<=int(a[1])+1) or (int(b[0])-1<=int(a[0])-1 and int(a[1])+1<=int(b[1])+1):
    total+=1

print(total)
    
