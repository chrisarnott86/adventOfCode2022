with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

bagtot=0
bags=[]
for line in lines:
    if line!="":
        bagtot+=int(line)
    else:
        bags.append(bagtot)
        bagtot=0
#print(bags)
bags.sort(reverse=True)
#print(bags)
print(sum(bags[0:3]))
