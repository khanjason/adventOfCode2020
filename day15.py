li=[16,11,15,0,1,7]
d={} #record when last spoken and last last# link turns to numbers
d2={} #link numbers to list of turns
s=set()
# if prev not in set, yield 0
#else diff
first=False
turn=0
for i in range(1,len(li)+1):
    d[i]=[li[i-1]]
    d2[li[i-1]]=[i]
    turn=turn+1
print(turn)
print(d)

last=li[-1]
#gen give turn, outputs spoken
def gen(n,first):
    if n<=len(li):
        s.add(li[n-1])
        first=True
        return [d[n],first]
    else:
        if first==True:
            first=False
            if 0 not in s:
                s.add(0)
                d2[0]=[n]
                first=True
            else:
                d2[0].append(n)
                first=False
            d[n]=[0]
            
    
            return [0,first]
        else:
            
            prev=d[n-1][-1] #last turn what was spoken, get prev
            
            time=d2[prev][-1]
            
            time2=d2[prev][-2]
            a=time-time2
            if a not in s:
                first=True
                s.add(a)
                d[n]=[a]
                d2[a]=[n]
                return [a,first]
            else:
                d[n]=[a]
                d2[a].append(n)
                first=False
                return [a,first]
t=False
#part1
for i in range(1,2021):
    r=(gen(i,t))
    t=r[1]
print(r[0])
t=False
#part 2 - brute force... it takes a min - change 2021 to 30000001




