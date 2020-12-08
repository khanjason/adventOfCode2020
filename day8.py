li=[]
done=[]
with open('day8input.txt') as f:
    l=f.readline()
    while l:
        t=l.split(' ')
        
        li.append(t)
        l=f.readline()

accum=0
last=len(li)
def execins(li,ind,accum):
    accum=accum
    #part1
    if ind in done:
        return ['fail',accum]
        return -1
    if ind==last:
        print(accum)
        return['pass',accum]
        
    done.append(ind)
    #print(accum)
    #print(li[ind])
    block=li[ind]
    ins=block[0]
    arg=block[1].replace('\n','')
    
    if ins=='acc':
        
        accum+=int(arg)
        return execins(li,ind+1,accum)
    elif ins=='jmp':
        offset=int(arg)
        return execins(li,ind+offset,accum)
    else:
        return execins(li,ind+1,accum)
    
#PART2    
def makecopy(li):
    l=[]
    for item in li:
        l.append(item)
    return l
a=0

done=[]
def getchange(li,n,swap1,swap2):
    copy=makecopy(li)
    
    if copy[n][0]==swap1:
        
        copy[n][0]=swap2
    return copy
valids=[]

for i in range(0,len(li)):
    done=[]
    a=0
    c=getchange(li,i,'jmp','nop')
    
    r=execins(c,0,a)
    if r[0]!='fail':
        valids.append(c[i])
        print(r)#answer here
    c=getchange(li,i,'nop','jmp')

#print(valids)

#part 1 run function
#print(execins(li,0,accum))
