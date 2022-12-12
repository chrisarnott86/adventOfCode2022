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

X = 1
cycles = 0
signalStrength = 0
        
signalStrength=0
display=[[' ' for _ in range(40)] for _ in range(6)]

for op in ops:      
    if op==0:
        cycles += 1
        if X==((cycles%40)-1):
            display[cycles//40][(cycles%40)-1]='#'
        elif X-1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        elif X+1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        continue
    else:
        cycles += 1
        if X==((cycles%40)-1):
             display[cycles//40][(cycles%40)-1]='#'
        elif X-1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        elif X+1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        cycles += 1
        if X==((cycles%40)-1):
             display[cycles//40][(cycles%40)-1]='#'
        elif X-1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        elif X+1==((cycles%40)-1):
             display[(cycles//40)][(cycles%40)-1]='#'
        X += op
   
for row in display:
    print("".join(row))
