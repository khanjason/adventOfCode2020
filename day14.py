li=[]
mems=[]
masks=[]
with open('day14input.txt') as f:
    l=f.readline()
    while l:
        li.append(l.strip())
        if 'mask' in l:
            masks.append(l.strip())
        if 'mem' in l:
            mems.append(l.strip())
        l=f.readline()
#print(mems)

def getlocations():
    locs=[]
    for m in mems:
        s=''
        start=False
        for c in m:
            
            
            if c=='[':
                
                start=True
            elif c==']':
                start=False
            elif start==True:
                
                
                
                s=s+c
            
            
        locs.append(int(s))
    return locs
locs=getlocations()
maxi=(max(locs))
            


def createmem(space):
    m=[0]*(space+1)
    return m

def writetomem(mem,val,ind):
    mem[ind]=val
    return mem

def applymask(mask,val):
    inds={}
    for n in range(len(mask)):
        if mask[n]!='X':
            inds[n]=mask[n]
    for k,v in inds.items():
        val[k]=v
    return val
def todec(s):
    s=s[::-1]
    c=0
    tot=0
    for b in s:
        if b==1 or b=='1':
            tot=tot+pow(2,c)
        c=c+1
    return(tot)
            

def tobin(n):
    b=[0]*36
    bs=''
    while n>=1:
        if n%2==1:
            bs=bs+'1'
        else:
            bs=bs+'0'
        n=int(n/2)
    for item in range(len(bs)):
        b[item]=int(bs[item])
    return b[::-1]

memory=createmem(maxi)
#part1
mas=0
for i in range(len(li)):
    if i==0:
        mas=(li[0].split('='))[1].strip()
    else:
        if li[i][:4]=='mask':
            mas=(li[i].split('='))[1].strip()
        else:
            s=''
            start=False
            for c in li[i]:
            
            
                if c=='[':
                
                    start=True
                elif c==']':
                    start=False
                    break
                elif start==True:
                    s=s+c
            ind=int(s)
            
            tmp=li[i].split('=')
            vt=int(tmp[1].strip())
            val=tobin(vt)
            val=applymask(mas,val)
            memory=writetomem(memory,val,ind)
#counting
ssum=0
for box in memory:
    
    if box!=0:
       ssum+=todec(box)
print(ssum)
from itertools import combinations_with_replacement,product
#part2

memory={}
def applymask2(mask,val):
    inds={}
    for n in range(len(mask)):
        if mask[n]=='X':
            #floating
            inds[n]=mask[n]
        elif mask[n]==1 or mask[n]=='1':
            inds[n]=int(mask[n])
    for k,v in inds.items():
        val[k]=v
    return val
#apply mask to memory address

#get string of x's
#form bin product
#write to mask
#form list
def copy(li):
    p=[]
    for t in li:
        p.append(t)
    return p


def getaddresses(mask,dec):
    addr=[]
    a=tobin(dec)#list
    a=applymask2(mask,a)
    inds=[]
    for item in range(len(a)):
        if a[item]=='X':
            inds.append(item)
    c=product('10', repeat=a.count('X'))
    for t in list(c):
        cop=copy(a)
        for ti in range(len(t)):
            
            cop[inds[ti]]=int(t[ti])
        addr.append(cop)
    return addr



    
mas=0
for i in range(len(li)):
    
    if i==0:
        mas=(li[0].split('='))[1].strip()
    else:
        if li[i][:4]=='mask':
            mas=(li[i].split('='))[1].strip()
        else:
            s=''
            start=False
            for c in li[i]:
            
            
                if c=='[':
                
                    start=True
                elif c==']':
                    start=False
                    break
                elif start==True:
                    s=s+c
            ind=int(s)
            ads=getaddresses(mas,ind)
            
            tmp=li[i].split('=')
            vt=int(tmp[1].strip())
            val=tobin(vt)
            
            for ad in ads:
                a=todec(ad)
                
                memory=writetomem(memory,val,a)
#counting
ssum=0
for k,box in memory.items():
    
    if box!=0:
       ssum+=todec(box)
print(ssum)

