
file_read = open('fileproject.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('fileproject.txt', 'w')
file_write.write(" File in write mode ....")
file_write.write("Hi! I am lia. My favorite subject is math ")
file_write.close()


file_append = open('fileproject.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("Hi! I am lia. My favorite subject is math")
file_append.close()

