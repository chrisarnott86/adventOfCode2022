import numpy as np
with open('input9.txt','r') as file:
#with open('input9-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

moves=[]
dirs={'R':np.array([1,0]) ,'L':np.array([-1,0]),'U':np.array([0,1]),"D":np.array([0,-1])}

for line in lines:
    moves.append((dirs[line.split()[0]],int(line.split()[1])))
 
knotPos, headPos = np.array([0,0]),np.array([0,0])

def getMoveVector(thisDiff):
    magnitude=np.linalg.norm(thisDiff)
    if magnitude==2.0:
        return np.array([thisDiff[0]/magnitude,thisDiff[1]/magnitude])
    # diagonal distance is 2.23606797749979
    elif magnitude>2.2:
        return np.array([thisDiff[0]/abs(thisDiff[0]),thisDiff[1]/abs(thisDiff[1])])    
    
def moveTail(head,tail):
    diff=head-tail
    # touching if distance is one (or 1.4142135623730951)
    # if touching do nothing, else move tail by unit vector
    # in correct direction
    if np.linalg.norm(diff)<1.5:
        return tail
    else:
        return tail+getMoveVector(diff)

allLocs=set()
for move in moves:
    for _ in range(move[1]):
        headPos+=move[0]
        knotPos=moveTail(headPos,knotPos)
        allLocs.add((knotPos[0],knotPos[1]))
        
print(len(allLocs))
        
