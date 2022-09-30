
ans = 7
guess_num = int(input("Enter your Guess:"))

if guess_num!=ans:
    if guess_num< ans:
        print("guess a higher number")
    else:
        print("Guess a lower number")
    guess_num = int(input())
    if guess_num == ans:
        print("You are correct")
    else:
        print("You are wrong")
else:print("You guessed correct number")            



         
  


