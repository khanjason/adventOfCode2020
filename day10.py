li=[]
from itertools import combinations
import operator as op
from functools import reduce
import math
diff=[]
with open('day10input.txt') as f:
    l=f.readline()
    while l:
        li.append(int(l))     
        l=f.readline()
#print(li)
        
m=max(li)+3
li.append(m)
#keep a list of possibilities
d=[]
start=0
countones=0
countthrees=0

sorts=sorted(li)
for n in range(0,len(sorts)):
    if n==0:
        if sorts[n]==1:
            countones+=1
        elif sorts[n]==3:
            countthrees+=1
            
            
        prev=sorts[n]
    else:
        if(sorts[n]-prev)==1:
            countones+=1
        elif sorts[n]-prev==3:
            countthrees+=1
            
        prev=sorts[n]

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

print(countthrees)
print(countones)
print(countones*countthrees)
#COMBS
#if diff is 3, theres no branch
#else, add a count
minlen=int(len(sorts)/3)

#find the base- all 3s
#then add extras
'''
base=[0]
while base[-1]<max(sorts):
    if base[-1]+3 in sorts:
        base.append(base[-1]+3)

    elif base[-1]+2 in sorts:
        base.append(base[-1]+2)
    else:
        ind=sorts.index(base[-1])
        base.append(sorts[ind+1])
#print(base)'''
base=[]
with open('base.txt') as b:
    tmp=b.readline()
    while tmp:
        a=[]
        for i in tmp.strip().split(','):
            if i!='':
                a.append(int(i))
        base.append(a)
        tmp=b.readline()
print(len(sorts)-len(base))
print(base)

for item in range(1,len(sorts)):
    if sorts[item]-sorts[item-1]==3:
        print(sorts[item],sorts[item-1])
#send these pairs as array
def diff(group):
    a=[]
    for item in range(1,len(group)):
        a.append(abs(group[item-1]-group[item]))
    return a

print(diff(sorts))

def arrange():
    

'''
left=2
for pi in sorts:
    if pi not in base:
        left+=1
print(left)
tot=1
for i in range(1,left+1):
    tot+=ncr(left,i)
#40 choose 1, 40 choose 2, ... until 40 choose 40
print(tot)
#1099511627776 is too low
tot=1

#67
print(len(li)-67+1)
#2199023255552 is too low
#not 4398046511104
'''
