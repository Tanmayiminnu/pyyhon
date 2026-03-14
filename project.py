file   = open("txt.txt","r")
print(file.read())
file.close()

file = open("txt.txt", "r")
print("\n Read in parts\n")
print(file.read(8))
file.close()

file = open("txt.txt","a")
file.write("Binary code represents these on and off signals as the digits 1 and 0. In order to make binary code manageable, computer programming languages were formed.")
file.close()


file = open("txt.txt",'r')
print("Reading first line...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("txt.txt",'r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()