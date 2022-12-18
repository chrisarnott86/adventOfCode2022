with open('input18.txt','r') as file:
#with open('input18-test.txt','r') as file:
#with open('input18-test2.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

cubes=[]
for line in lines:
    cubes.append((int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])))


def getFaces(cube):
    theFaces=[]
    #down
    theFaces.append(frozenset([
                     (cube[0],cube[1],cube[2]),
                     (cube[0]+1,cube[1],cube[2]),
                     (cube[0],cube[1],cube[2]+1),
                     (cube[0]+1,cube[1],cube[2]+1)]))
    #up
    theFaces.append(frozenset([
                     (cube[0],cube[1]+1,cube[2]),
                     (cube[0]+1,cube[1]+1,cube[2]),
                     (cube[0],cube[1]+1,cube[2]+1),
                     (cube[0]+1,cube[1]+1,cube[2]+1)]))
    #left
    theFaces.append(frozenset([
                     (cube[0],cube[1],cube[2]),
                     (cube[0],cube[1]+1,cube[2]),
                     (cube[0],cube[1],cube[2]+1),
                     (cube[0],cube[1]+1,cube[2]+1)]))                     
    #right
    theFaces.append(frozenset([
                     (cube[0]+1,cube[1],cube[2]),
                     (cube[0]+1,cube[1]+1,cube[2]),
                     (cube[0]+1,cube[1],cube[2]+1),
                     (cube[0]+1,cube[1]+1,cube[2]+1)]))
    #front
    theFaces.append(frozenset([
                     (cube[0],cube[1],cube[2]),
                     (cube[0]+1,cube[1],cube[2]),
                     (cube[0],cube[1]+1,cube[2]),
                     (cube[0]+1,cube[1]+1,cube[2])]))
    #back
    theFaces.append(frozenset([
                     (cube[0],cube[1],cube[2]+1),
                     (cube[0]+1,cube[1],cube[2]+1),
                     (cube[0],cube[1]+1,cube[2]+1),
                     (cube[0]+1,cube[1]+1,cube[2]+1)]))
    return theFaces                                   
                     
faces=set()  
for cube in cubes:
    myFaces=getFaces(cube)
    for face in myFaces:
        if face in faces:
            faces.remove(face)
        else:
            faces.add(face)
      
#print(faces)  
print(len(faces))
