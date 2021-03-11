myfile = open("new.txt","w")
myfile = open("new.txt","r")
cont = myfile.read()
print(cont)
myfile.close()
file = open("new.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()
