#operation on file

f=open("Preamble.txt")      #opening a file using relative path and using a pointer
text=f.read()                #reading a file
print(text)                  #printing the output

###############################################################

f=open("D:\\MyData\Desktop\python\Preamble.txt")  #opening a file using path
text=f.read()                                     #reading a file
print(text)                                       #printing the output