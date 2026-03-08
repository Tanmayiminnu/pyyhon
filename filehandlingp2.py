file_read = open("codingal.txt","r")
print("file in read mode -")
print(file_read.read())
file_read.close()

file_write = open("codingal.txt","w")
file_write.write("File in write mode....")
file_write("Hi! I am penguin.I am 1yr. old")
file_write.close()

file_append = open("codingal.txt", "a")
file_append.write("File in append mode ....")
file_append.write("hi! I am penguin.I am 1yr. old")
file_append.close()