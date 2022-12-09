file = open('message.txt', 'r')
letters=[]
i=0

while True:
  i=i+1
    # read by character
  char = file.read(1)
  letters.append(char)
  if len(letters)>14:
    letters.pop(0)
    m= list(set(letters))
    #print(i,letters)

    if (len(m)==14):
      print('yay',i)
      break
    
  
  

  if not char:#if no char
    break
         
  #print(char)
file.close()
