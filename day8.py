
# Sets
#How to create a set

evenNo={12,14,16,18,20,22,24,26,28,30}
oddNo={31,33,35,37,39,41,43,45,47,49}

print(evenNo)# output will not be the saqme order as we have enterted the value
print(oddNo)# output will not be the saqme order as we have enterted the value

numberA=("action",)# it is tuple,if no of elments is one and comma given after element,here element is string
print(type(numberA))

numberB=(7,)# it is tuple,if no of elments is one and comma given after element,here element is integer
print(type(numberA))



oddNo1 = {} # this is an empty set so called as= dictionary
print(oddNo1)
print(type(oddNo1))

# Checking the properties of Serts
evenNo1 = {42.44,46,48,50,42,52,54,48}# we get only unique values in the set and not repeat values
print(evenNo1)# output will not be in the same order as we have entered the value
print("length of Even is")
print(len(evenNo1))

#******************************Methods**********************************
print("************************Methods*********************************")

evenNo3= {62,64,66,68}
evenNo3.add(70)# to insert single element in set,its sequence wiil be random
print(evenNo3)

oddNo3={71,73,75,77}
evenNo3.update(oddNo3)# To insert complete set in each other,sequence of elements will be random
print(evenNo3)

numC = {100,200,300,400,500,600,700,800,900}
print(numC.remove(500))
print(numC)

print(numC.discard(800))
print(numC)

print(numC.discard(540))
print(numC)# No error by discard method even if the element is absent

#print(numC.remove(230))# remove method give error to remove absent element
#print(numC)

#*****************pop**********************

#numD = {81,82,83,84,85,86,87,88,89}
#print(numD.pop(4))# This will throw error,because in pop method we should not give arggument,it should be blank
#print(numD)

numE = {91,92,93,94,95,96,97,98,99}
print(numE.pop())# Any random item will be deleteb from set
print(numE)

print(numE.pop())
print(numE)

print(numE.pop())
print(numE)

print(numE.pop())
print(numE)


print(numE.pop())
print(numE)

print(numE.pop())
print(numE)

print(numE.pop())
print(numE)

print(numE.pop())# Single element remained
print(numE)

print(numE.pop())
print(numE)



#By using pop method we can remove all elements from set,it gives empty set in last
# By using pop method on empoty set,we get output as no element remained in set
#i.e.we get 'pop from an empty set error'


numE.clear()# we get empoty set by clear method#we don;t get error here by clear method
print(numE)

numE.clear()
print(numE)

#*********************************************
even1 = {2,4,6,8}
print(even1)# we can use this to find output
#even1.print()# we can't use this to find output it throws error















