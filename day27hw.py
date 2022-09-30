

print("with.lstrip()")
with open('indent.txt') as W:
    for line in W:
        print(line.lstrip())

print('*********************************')

print("with.rstrip()")
with open('indent.txt')as W:
    for line in W:
        print(line.rstrip())

print('*********************************')

print("with.strip()")
with open('indent.txt')as W:
    for line in W:
        print(line.strip())