#from numpy import loadtxt

with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

maxelf=0
bagtot=0
for line in lines:
    #print(line)
    if line!="":
        bagtot+=int(line)
    else:
        if(bagtot>maxelf):
            maxelf=bagtot
        bagtot=0
print(maxelf)
