file = open('message.txt', 'r')
letters=[]
i=0

while True: #while there are character in the txt it will be true. 
  i=i+1 # using this as a counter so I know which character. 
    # read by character
    
  char = file.read(1)
  letters.append(char) # letters will store the last 3 character in addition to the current char.
  if len(letters)>4:
    letters.pop(0) # removes the first char so that there are 4 again. 
    #print(i,letters)  # just used to see what number the last one that was added was and what the 4 chars are. 
    
    m= list(set(letters)) # this will squish the list by removing duplicates.


    if (len(m)==4):# means that these are all unique, because other wise the list would not be 4 letters after being squished. 
      print('yay',i) 
      break # so it doesn't do the rest. 
    
  
  

  if not char:#if no char
    break
         
  #print(char)
file.close()
