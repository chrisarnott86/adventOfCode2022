with open('input5.txt','r') as file:
#with open('input5-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.replace('\n','') for line in lines]

section='initial'
moves=[]
# stacks is 3 for test and 9 for real
numstacks=9
#numstacks=3
stacks=[[] for i in range(numstacks)]
for line in lines:
    if line[:2]==' 1':
        continue
    if line=='':
        section='moves'
        continue
    if section=='initial':
        for i in range(numstacks):
            if line[4*i+1]!=' ':
                stacks[i].append(line[4*i+1])           
    if section=='moves':
        moves.append((int(line.split()[1]),int(line.split()[3])-1,int(line.split()[5])-1))

for stack in stacks:
   stack.reverse()

for move in moves:
    for i in range(move[0]):
        stacks[move[2]].append(stacks[move[1]].pop())

output=''
for i in range(numstacks):
    output+=stacks[i].pop()
    
print(output)
