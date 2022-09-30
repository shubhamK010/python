# Creating Sample List
#          0   1   2   3    4    5     6    7    8
numList_1=[0  ,1  ,2  ,3   ,4   ,5    ,6   ,7   ,8    ,9  ]
print(numList_1)
print(len(numList_1))


print("**************************")

#Accessing the individual items in the last
print(numList_1[5])
print(numList_1[4])
print(numList_1[9])
print(numList_1[2])


print("********************************")
print(numList_1[3:9]) # last index do not print
print(numList_1[2:6])
print(numList_1[0:]) # we didnt give second digit so it will print till end of list
print(numList_1[:7]) # here we didnt give first digit so it will consider from start

print("****************************")

#               0           1           2        
numList_2 = ["Ironman1","Ironman2","Ironman3"]
print(len(numList_2))
print(numList_2[0:2])
print(numList_2[1:3])

numList_1[7:9]=[77,88,99,109]
print(numList_1)

#Append at the end of the list

print("***********************************")
numList_2.append("Ironman4")
print(numList_2)

#Insert at the given index position and the current itm will shift one position to right

print("**************Insert*****************")
numList_2.insert(2,"Hulk3")
print(numList_2)


# Extend is used to join two lists

print("*******************Extend*****************")
numList_2 = ["Ironman1","Ironman2","Ironman3"]
numList_3 = ["Hulk1","Hulk2","Hulk3"]
numList_2.extend(numList_3)
print(numList_2)
print(numList_2+numList_3) # it is also called as concatenation

#            0 1 2  3  4  5  6  7
numList_1 = [3,6,40,9,12,15,45,18,21,20,24]
print(numList_1)
print(len(numList_1))

# Methods in list
# Sort
numList_1.sort()
print(numList_1)

# Reverse---This will print in descending order
numList_1.sort(reverse=True)
print(numList_1)

#Making copy of original 
num_copy=numList_1.copy()
print("***************This is Copy***************")
print(num_copy)

#remove---Removing actual item from the last
num_copy.remove(9)
print(num_copy)
num_copy.remove(20)
print(num_copy)

#pop---remove last item in the list when no index is given
print("****************pop******************")
num_copy.pop()
print(num_copy)

#pop---used to remove index item in the list
num_copy.pop(5)
print(num_copy)

#clear
num_copy.clear()
print(num_copy)
print(len(num_copy))














#**************H.W.***********************

#Q.1.Sum of items in list containinig all one digit prime numbers

primeNum = [2,3,5,7]
sum = sum(primeNum)
print("sum of one digit prime numbers:",sum)

#Q.2.Taking marks scored by ten students as input to a list and checking
# how many has scored 100

marks=[50,100,98,76,100,36,80,70,35,66]
century=marks.count(100)
print("100 marks scored by",century,"students")


                                                                                                                                                                                                                                                                














