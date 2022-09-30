#Todays Code


#****************************************************

# CREATING A DICTIONARY 
work1 = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five"
}


print(work1)

# Duplicate Values and Order of Data
# Duplicate Values

work1 = {
    1 : "one",
    2 : "two",
    3 : "three",
    5 : "five+",
    4 : "four",
    5 : "five" #ye latest value hai isliye output me dikhega
}

# Accessing a dictionary
# Using key as index method( we us eindex here)

print(work1[1])
aa = work1[1]
print(aa)
bb = work1[5]
print(bb)
#cc = work1[9] # ACCESSING VALUE WHICH DOES NOT EXIST WILL GIVE ERROR(jo value nhi hai wo error de degi)
#print(cc)
#dd=work1[8]
#print(dd)

# USING GET METHOD

print(work1.get(3))
print(work1.get(0)) # ACCESSING VALUE WHICH DOES NOT EXIST WONT GIVE ERROR(isme bhi jo exist nhi karta uske liye 'none' de dega)