with open('input2.txt','r') as file:
#with open('input2-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

moves={'X':1,'Y':2,'Z':3}
results={'AX':3,'BY':3,'CZ':3,
        'AZ':0,'BX':0,'CY':0,
        'AY':6,'BZ':6,'CX':6}

sumbo=0
for line in lines:
    opp=line.split(' ')[0]
    me=line.split(' ')[1]
    sumbo+=(moves[me])
    sumbo+=(results[opp+me])

    #print(moves[me],' ',results[opp+me])

print(sumbo)
