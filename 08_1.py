with open('input8.txt','r') as file:
#with open('input8-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

treemap=[]
for line in lines:
    treemap.append([int(char) for char in line])

def isVisible(i,j,mymap):
    visible=False
    # need to look left, right, up and down
    # Left
    if mymap[i][j]==max(mymap[i][:j+1]) and len([x for x in mymap[i][:j+1] if x==max(mymap[i][:j+1])])==1:
        visible=True
    # Right
    if mymap[i][j]==max(mymap[i][j:]) and len([x for x in mymap[i][j:] if x==max(mymap[i][j:])])==1:
        visible=True
    # Down
    tempcol=[row[j] for row in mymap]
    if mymap[i][j]==max(tempcol[i:]) and len([x for x in tempcol[i:] if x==max(tempcol[i:])])==1:
        visible=True
    # Up
    if mymap[i][j]==max(tempcol[:i+1]) and len([x for x in tempcol[:i+1] if x==max(tempcol[:i+1])])==1:
        visible=True        

    return visible
    
visTrees=0
for i,row in enumerate(treemap):
    for j,column in enumerate(row):
        if i==0 or i==len(row)-1 or j==0 or j==len(row)-1:
            continue
        visTrees+=1 if (isVisible(i,j,treemap)) else 0

perimeterTrees=4*(len(treemap[0])-1)
print(visTrees+perimeterTrees)
