

months_A= {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}

months_B = {"Feb"} # have only one element

months_C = {"Jan", "Mar", "May","Jul", "Aug", "Oct", "Dec"}

months_D = {"Apr", "Jun", "Sep", "Nov"}


print(len(months_A))
print(len(months_B))
print(len(months_C))
print(len(months_D))


# To get the common elements in the set

print(months_A.intersection(months_B)) # BETWEEN TWO SETS

print(months_D.intersection(months_B,months_A)) # BETWEEN THREE SETS

k =  months_B.intersection(months_B,months_D) # THE INTERSECTION RESULT CAN BE STORED IN A VARIABLE
print(k)
print(type(k))


# TO GET THE UN-COMMON ELEMENTS IN THE SET 
print(months_D.symmetric_difference(months_B))
print(months_A.symmetric_difference(months_C))





















































