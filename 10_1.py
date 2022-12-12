with open('input10.txt','r') as file:
#with open('input10-test.txt','r') as file:
#with open('input10-test2.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

ops=[]

for line in lines:
    if 'noop' in line:
        ops.append(0)
    else:
        ops.append(int(line.split()[1]))

#print(ops)
X = 1
cycles = 0
signalStrength = 0
        
signalStrength=0
for op in ops:      
    if op==0:
        cycles += 1
        if (cycles==20 or (cycles+20)%40==0):
            print(cycles,X,X*cycles)
            signalStrength+=X*cycles
        continue
    else:
        cycles += 1
        if (cycles==20 or (cycles+20)%40==0):
            print(cycles,X,X*cycles)
            signalStrength+=X*cycles
        cycles += 1
        if (cycles==20 or (cycles+20)%40==0):
            print(cycles,X,X*cycles)
            signalStrength+=X*cycles        
        X += op

print(signalStrength)
