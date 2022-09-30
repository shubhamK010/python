#HW
####################################
# run the reaction game and share the Output

# reaction game 

import time
import random

input(" Press Enter to start the Game ")
wait_time = random.randint(1 ,6) # this will generate random num from 1 to 6
# print(wait_time)
time.sleep(wait_time)
start_time = time.time()


input(" Press Enter to stop the Game ")
stop_time = time.time()
print(stop_time - start_time)
