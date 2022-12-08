with open('input8.txt','r') as file:
#with open('input8-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

treemap=[]
for line in lines:
    treemap.append([int(char) for char in line])

def scenicScore(i,j,mymap):
    visible=False
    # need to look left, right, up and down
    # Left
    myHeight=mymap[i][j]
    leftSlice=mymap[i][:j]
    leftSlice.reverse()
    leftScore=0
    for val in leftSlice:
        if val==myHeight:
            leftScore+=1
            break
        elif val<myHeight:
            leftScore+=1
        else:
            leftScore+=1
            break
    # Right
    rightSlice=mymap[i][j+1:]
    rightScore=0
    for val in rightSlice:
        if val==myHeight:
            rightScore+=1
            break
        elif val<myHeight:
            rightScore+=1
        else:
            rightScore+=1
            break           
    # Down
    tempcol=[row[j] for row in mymap]
    downSlice=tempcol[i+1:]
    downScore=0
    for val in downSlice:
        if val==myHeight:
            downScore+=1
            break
        elif val<myHeight:
            downScore+=1
        else:
            downScore+=1
            break           
    # Up
    tempcol=[row[j] for row in mymap]
    upSlice=tempcol[:i]
    upSlice.reverse()     
    upScore=0
    for val in upSlice:
        if val==myHeight:
            upScore+=1
            break
        elif val<myHeight:
            upScore+=1
        else:
            upScore+=1
            break           
    return leftScore*rightScore*upScore*downScore
    
maxScore=0
for i,row in enumerate(treemap):
    for j,column in enumerate(row):
        if i==0 or i==len(row)-1 or j==0 or j==len(row)-1:
            continue    
        tempScore=scenicScore(i,j,treemap)
        if tempScore>maxScore:
            maxScore=tempScore
print(maxScore)
