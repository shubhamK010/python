#unpacking a list
list1 = [1,2,3,4,5]

# print(list1[0])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# a , b ,c , d,e = [1,2,3,4,5] # unpacking a list 

list1 = [1,2,3,4,5]
a , b ,c , d,e = list1 
print(a)





# using print () to write a file 
# we have been given below data to write in a text file 

data = [
"abhi - Pass",
"ram dutt gupta - Fail",
"khadak singh - Pass",
"gurmit singh - Fail",
"chanderpal - Pass",
"aman - Pass",
"khursid - Fail",
"rajeev - Pass",
"durgesh - Fail",
"nahar singh - Pass",
"ram kumar - Fail",
"sunder paal - Pass"
]


# with open('Report_card3.txt' ,'w') as f:
#     for row in data:
#         print(row, file=f)


# print(f.mode)
# print(f.read)

# using pass in content manager to create an empty file 
with open('Report_card3.txt' ,'w') as f:
    # for row in data:
    #     print(row, file=f)
    pass

# using write () method to write a file 
# we have been given below data to write in a text file 

data = [
"abhi - Pass",
"ram dutt gupta - Fail",
"khadak singh - Pass",
"gurmit singh - Fail",
"chanderpal - Pass",
"aman - Pass",
"khursid - Fail",
"rajeev - Pass",
"durgesh - Fail",
"nahar singh - Pass",
"ram kumar - Fail",
"sunder paal - Pass"
]

with open("Report_card_write_2", 'w') as f:
    for row in data:
        # TO WRITE THE DATA IN FILE
        f.write(row)
    # to confirm the data we are printing on the terminal
    print(data)


# to create a blank file

with open("Report_card_write_Empty", 'w') as f:
    pass