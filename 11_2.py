import re

#with open('input11.txt','r') as file:
with open('input11-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


    
class Monkey:
    def __init__(self, items, operation, testDivisor, targets):
        self.items = items
        self.operation = operation  
        self.testDivisor = testDivisor
        self.targets = targets
        self.inspects = 0
    
    def evalOperation(self,operation,item):
        if isinstance(operation[1],int):
            if operation[0]=='*':
                return item * operation[1]
            if operation[0]=='+':
                return item + operation[1]                
        else:
            return item * item
    
    def updateWorry(self,item):
        item = self.evalOperation(self.operation,item)
#        item = item//3
        return item
        
    def receiveItem(self,item):
        self.items.append(item)
        
    def haveTurn(self):
        self.items.reverse()
        while (len(self.items)>0):
            self.inspects+=1
            item=self.items.pop()
            item = self.updateWorry(item)
            if (item%self.testDivisor==0):
                monkeys[self.targets[0]].receiveItem(item)
            else:
                monkeys[self.targets[1]].receiveItem(item)
                
    def showItems(self):
        print(self.items)

    def showInspects(self):
        return self.inspects

monkeys=[]
for line in lines:
    if 'Monkey' in line:
        tempItems=[]
        tempOps=[]
        tempTargets=[]
        continue
    if 'Starting' in line:
        tempItems.extend([int(i) for i in line.split(': ')[1].split(', ')])
    if 'Operation' in line:
        tempOps.append(line.split(' = ')[1].split()[1])
        try:
            tempOps.append(int((line.split(' = ')[1].split()[2])))
        except:
            tempOps.append(line.split(' = ')[1].split()[2])
    if 'Test' in line:
        tempDivisor = int(re.findall("[0-9]+", line)[0])
    if 'true' in line:
        tempTargets.append(int(re.findall("[0-9]", line)[0]))
    if 'false' in line:
        tempTargets.append(int(re.findall("[0-9]", line)[0]))
        monkeys.append(Monkey(tempItems,tempOps,tempDivisor,tempTargets))
        

for rounds in range(50):
    for i,monkey in enumerate(monkeys):
        if (i==0):
            print("Round:",rounds+1," Monkey",i, monkey.showInspects())
        monkey.haveTurn()

allInspects=[]
for monkey in monkeys:
    allInspects.append(monkey.showInspects())

allInspects.sort()
print(allInspects)
print(allInspects[-1]*allInspects[-2])


