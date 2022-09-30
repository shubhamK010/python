
# PARSING DATA = MAKING SENSE OF DATA = UNDERSTANDING THE DATA 

with open('tiger_india.txt') as f:
    for row in f:
        # print(row)
        data = row.strip('\n').split("|")
        States, Capital, Tigers = data
        print(States,Capital,Tigers , sep="\n\t")
        # print(data)



# we can use this data to check the count of tigers
# we can also store this data and use as search for state wise count



f =  open('tiger_india.txt')
text = f.read()
print(text)
f.close()
# check if the file is closed
print(f.closed) 
 # default mode is "read"
print(f.mode)