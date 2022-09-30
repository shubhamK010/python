
# HW Only Observe the Output
print("****without  continue ******")
for i in range(10):
    
    if i % 2 == 0 and i!=0: # Check if i is even (also removing 0 as it is divisible by 2 )
        print(i)


print("***with continue *******")
for i in range(10):
    
    if i % 2 == 0 : # Check if i is even
        continue #but this will skip the next line if the condition is TRUE
    print(i)