cups=[7,1,6,8,9,2,5,4,3]
for n in range(10,1000001):
    cups.append(n)
curr=0

for i in range(0,10000000):
    #print('move ',i+1)
    #print(cups)
    #print('current: ',cups[curr])
    if curr+1<len(cups):
        first=cups[curr+1]
    else:
        first=cups[1-(len(cups)-curr)]
    if curr+2<len(cups):
        second=cups[curr+2]
    else:
        second=cups[2-(len(cups)-curr)]
    if curr+3<len(cups):
        third=cups[curr+3]
    else:
        third=cups[3-(len(cups)-curr)]
        
    picked=[first,second,third]
    #print('picked up: ',picked)
    hold=cups[curr]
    cups.remove(first)
    cups.remove(second)
    cups.remove(third)
    i=1
    mi=min(cups)
    wrap=False
    #print((cups))
    while hold-i not in cups:
        
        i=i+1
        
        if hold-i < mi:
            
            wrap=True
            break
    if wrap==True:
        #print('ok')
        dest=cups.index(max(cups))
    else:
        dest=cups.index(hold-i)
    #print('destination: ',cups[dest])
    #gold=cups[curr]
    cups.insert(dest+1,first)
    cups.insert(dest+2,second)
    cups.insert(dest+3,third)
    if cups.index(hold)<len(cups)-1:
        curr=cups.index(hold)+1
    else:
        curr=0
print('final')
ind=cups.index(1)
print(cups[ind+1])
print(cups[ind+2])
#print(cups)
