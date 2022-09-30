

#data = [1,2,3,4,5]


# with open('Numbers_print.txt','w') as f:
#     for row in data:
#         print(row,file=f)

data = ('1','2','3','4','5')

with open("Numbers_print.txt",'w') as f:
    for row in data:
        f.write(row)
































