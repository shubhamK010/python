# HW practise
#################################################


# Q1. calculate the execution time by using time.time() for 1st Code and 2nd Code and observe the difference
# Q2. calculate the execution time by using time.process_time() for 1st Code and 2nd Code and observe the difference

# 1st Code 
# x=0
# sum = 0
# while (x<11000):
#      sum=sum+x
#      x=x+1
# print(sum)
        


# 2nd Code
sum =0
for i in range(11000):
     sum=sum+i
print(sum)