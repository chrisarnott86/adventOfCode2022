with open('input2.txt','r') as file:
#with open('input2-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

moves={'A':1,'B':2,'C':3}
moves2={'X':0,'Y':3,'Z':6}
results={'AX':'C','BX':'A','CX':'B',
         'AY':'A','BY':'B','CY':'C',
         'AZ':'B','BZ':'C','CZ':'A'}

sumbo=0
for line in lines:
    opp=line.split(' ')[0]
    res=line.split(' ')[1]
    me=results[opp+res]
    #print(me)
    sumbo+=(moves[results[opp+res]])
    sumbo+=(moves2[res])

    #print(moves[me],' ',results[opp+me])

print(sumbo)
