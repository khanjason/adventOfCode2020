li=[]
with open('day1input.txt') as f:
    t=f.readline()
    while(t):
        if '\n' in t:
            t=t[:-1]
        li.append(int(t))
        t=f.readline()

#2 pointer
#print(li)
p1=0
p2=len(li)-1
tot=0
ans=[]
while tot!=2020:
    
    if p2==0:
        p2=len(li)-1
        p1=p1+1
    
    tot=li[p1]+li[p2]
    if tot==2020:
        ans.append(li[p1])
        ans.append(li[p2])
        break
    else:
        tot=0
        p2=p2-1
print(ans[0]*ans[1])




#3 pointer 
#print(li)
p1=0
p2=len(li)-1
p3=0
tot=0
ans=[]
while tot!=2020:
    if p1==len(li)-1:
        p1=0
        p2=len(li)-1
        p3=p3+1
    
    if p2==0:
        p2=len(li)-1
        p1=p1+1
    
    tot=li[p1]+li[p2]+li[p3]
    if tot==2020:
        ans.append(li[p1])
        ans.append(li[p2])
        ans.append(li[p3])
        break
    else:
        tot=0
        p2=p2-1
print(ans[0]*ans[1]*ans[2])
