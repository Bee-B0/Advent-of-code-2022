
total=0

txt= open('jobs.txt').readlines()
#print(txt)
for line in txt:
  line = line.strip('\n')
  pair= line.split(",")
  #print(pair)
  a=pair[0].split("-")
  #print(a)
  b=pair[1].split("-")
  #print(b)
  a1 = int(a[0])
  b1 = int(b[0])
  a2 = int(a[1])+1
  b2 =int(b[1])+1

  
  ## -1 so that the boundrys include the numbers.
  if len (set(range(a1,a2)) & set(range(b1,b2))) >0 :
    total+=1

print(total)
