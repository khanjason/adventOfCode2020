liinput=[]
with open ('day9input.txt') as f:
    l=f.readline()
    while l:
        liinput.append(l.strip())
        l=f.readline()
li=[]
for ti in liinput:
    li.append(int(ti))


def getpreambles(li,ind,prelen):
    output=[]
    if ind<=prelen:
        output=li[:ind]
    else:
        output=li[ind-prelen:ind]
    return output

ind=50
#print(getpreambles(li,ind,25))

#li is preamble
def twosum(lis,target):
    p1=0
    p2=len(lis)-1
    tot=0
    ans=[]
    while tot!=target:
        if p1==len(lis)-1:
            return False
        
        if p2==0:
            p2=len(lis)-1
            p1=p1+1
        
        tot=lis[p1]+lis[p2]
        
        if tot==target:
            return True
            
        else:
            tot=0
            p2=p2-1
#part1
for item in range(0,len(li)):
    p=getpreambles(li,item,25)
    
    if len(p)>24:
        if (twosum(p,li[item]))==False:
            print(li[item])
#part2
            

#target 32321523
#for i in li, iterate until the target is reached
targ=32321523
def iteratesum(ind,li,target):
    out=[]
    tot=0
    p=ind
    while tot<target:
        if tot>target:
            return []
        tot=tot+li[p]
        out.append(li[p])
        p=p+1
        if tot==target:
            return out
for n in range(0,len(li)):
    r=iteratesum(n,li,targ)
    if r !=[] and r!=None and len(r)>1 :
        sm=min(r)
        lar=max(r)
        print(sm+lar)
        
        
    


