## HW
#################################

# working with JSON : Limitations  OF JSON IN PYTHON 
# write below data in score_ipl.json file and then read the same json file
# check the data type each time while writing and then reading

import json
Points_ipl = (
("CSK",12),
("SRH",12),
("KXP",10),
("KKR",8),
("RCB",6),
("RR",6),
("MI",4),
("DD",4)
)   



# # writing a json file
# print(type(Points_ipl))

# with open('score_1.json','w', encoding='utf-8') as f:
#     json.dump(Points_ipl,f)

# reading a json file
print(type(Points_ipl))

with open('score_1.json','r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(type(data))
