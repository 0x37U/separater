print("\t[+] Separate the words on one line [+]") #Title name tool
text = input("Enter ur list : ") #input for ask u about list
def Sep(): #function
  readd = open(text,'r').read() #open and read text file
  chng = readd.replace(" ","\n") #Replace Space to new line
  with open ('words.txt','a+') as f: # open new file for put Separate words
    f.write(chng) # write in new file
  print(chng) #output Separate
Sep() #close function
