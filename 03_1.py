#with open('input3.txt','r') as file:
with open('input3-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

for line in lines:
    bagMiddle=len(line)//2
    bagA=line[0:(bagMiddle-1)]
    bagB=line[bagMiddle:]
    setA=set()
    setB=set()
    for char in bagA:
        setA.add(char)
    for char in bagB:
        setB.add(char)
        
    print(setA.intersection(setB))
