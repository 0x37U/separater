print("\t[+] Separate the words on one line [+]")
text = input("Enter ur list : ")
def Sep():
  readd = open(text,'r').read()
  chng = readd.replace(" ","\n")
  with open ('words.txt','a+') as f:
    f.write(chng)
  print(chng)
Sep()
