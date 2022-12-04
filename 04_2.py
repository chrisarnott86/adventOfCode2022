with open('input4.txt','r') as file:
#with open('input4-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

counto=0
for line in lines:
    elfA=(line.split(',')[0].split('-')[0],line.split(',')[0].split('-')[1])
    elfB=(line.split(',')[1].split('-')[0],line.split(',')[1].split('-')[1])
    setA=set([x for x in range(int(elfA[0]),int(elfA[1])+1)])
    setB=set([x for x in range(int(elfB[0]),int(elfB[1])+1)])

    if (len(setA.intersection(setB))!=0):
        counto+=1
        #print("got one")

print(counto)
