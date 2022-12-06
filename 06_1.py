with open('input6.txt','r') as file:
#with open('input6-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

for line in lines:
    for i,char in enumerate(line):
        if (len(set(char for char in line[i:i+4]))==4):
            print(i+4)
            break
