# Tuples
#How to create a tuple
#                  0       1       2       3       4       5      6        7
study_secrets1=("step1","step2","step3","step4","step5","step6","step7","step8")
print(study_secrets1)
print(type(study_secrets1))

study_secrets2=("step1","step2","step3","step4")
print(study_secrets2)
print(type(study_secrets2))


# Check the characteristics for single element/item and blank/none
study_secrets3=("step1")
print(study_secrets3)
print(type(study_secrets3))

## " ", is essential to make it a tuple without it will show as "string"


# Reading individual items/range of items from  tuple
print(study_secrets1[3])# single element
print(study_secrets1[0:6])# range of elements(dont give last element)
print(study_secrets1[0:2])
print(study_secrets1[0:5])

# Check if tuple is mutable(changable) or not

#study_secrets1[2]="step8"  # this will give throw error,because tuple object does not support item assignment
#print(study_secrets1.replace("step2")) #this will also throw error
# means tuple is immutable(not changable)

# Methods in Tuple, except for methods used to change element
#Methods of LIST also work here eg.sum(function)


study_secrets4=("step1","step2","step3","step4","step5","step6","step7","step8","step4")
print(study_secrets1)
print(type(study_secrets1))

## count and index methods for tuple
print(study_secrets4.count("step4")) #here pass the value of element

print(study_secrets4.index("step7")) #here output will be the index position

























































