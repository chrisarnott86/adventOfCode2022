#from numpy import loadtxt

#file=open('input1.txt','r')
#file=open('input1-test.txt','r')
#data = loadtxt('input.txt',dtype='int')
#data = file.read()
with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

#print(lines)
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

#count = 0
#temp1 = data[0]
#for i in data:
#    temp2 = i
#    if temp2>temp1:
#        count+=1
#    temp1=i

#print(count)
