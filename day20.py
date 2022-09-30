# revision for last class ====>

# i = 0
# while i<10:
#     print(i) # here we use print befoe incremnet and its ideal way so that i should not include last number i.e.10
#     i=i +1

# Using while loop when number of attempts are not known
# Exiting a location with four directions,but dont know how many times a user will guess

# available_exits = ["n","s","e","w"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Enter the direction to exit:").casefold()
# print("You have exited")    

# Using while lopp when number of attempts are not known
# Exiting a location with four directions,but dont know how many times a user will guess
#Using break in while loop.Player will quit the game

# available_exits = ["n","s","e","w"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Enter the direction to exit:").casefold()
#     if chosen_exit=="quit":
#         print("GAME OVER")
#         break
# print("You have exited")  

# Using while lopp when number of attempts are not known
# Exiting a location with four directions,but dont know how many times a user will guess
#Using break in while loop.Player will quit the game
#Using ELSE in the code

available_exits = ["n","s","e","w"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Enter the direction to exit:").casefold()
    if chosen_exit=="quit":
        print("GAME OVER")
        break
else:    
  print("You have exited")  