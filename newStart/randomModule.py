import random

# from 0 to 1 , need to generate some random numbers(int/floats)
# ans  = random.random()
# print(ans)

#  for integer values
# limits are included in the result

# ans  = random.randint(1,10)
# print(ans)


# selecting from a list 

# lucky_num = [10,25,24,2,88,79]
# ans = random.choice(lucky_num)
# print(ans)

# vit_c = ["lemon", "orange" ,"guava","blackberries","strawberries"]
# ans = random.choice(vit_c)
# print(ans)

# to select multiple random values from the given list
# ans = random.choices(vit_c , k=2)
# print(ans)


#################################################
#  TOSSING A COIN
#################################################

# import random

# list_ans = []
# for i in range(1,11):
#     list_coin = ["h" ,"t"]
#     ans  = random.choice(list_coin)
#     list_ans.append(ans)

# # print(list_ans)
# heads  = list_ans.count("h")
# print("Heads count is : " ,heads)
# tails  = list_ans.count("t")
# print("Tails count is : " ,tails)

#################################################
#  TOSSING A COIN
#################################################

# import random       
# # //yaha pe double import random yu hi likha hai ki koi error na aa jaye

# list_ans = []
# for i in range(1,11):

#     list_coin = ["h" ,"t"]
#     ans  = random.choice(list_coin)
#     list_ans.append(ans)
      

# print(list_ans)
# heads  = list_ans.count("h")
# print("Heads count is : " ,heads)
# tails  = list_ans.count("t")
# print("Tails count is : " ,tails)

# iske output me hum ye dekh sakte hai ki head or tail ka value 0 or  1 nahi aa raha hai



#################################################
#  USER DEFINED MODULE
#################################################

import randomModuleFile2

randomModuleFile2.minus()
print(randomModuleFile2.sum1(10,30))
print(randomModuleFile2.__name__)   #yaha randomModuleFile2 is file ka name print nahi hoga..khali file ka namm i.e.randomModuleFile2 ye print hoga
print(__name__)     #ye is file ka main hai i.e.randomModuleFile