rules=[]
myticket=[]
others=[]
yours=False
other=False
with open('day16input.txt') as f:
    l=f.readline()
    while l:
        if yours==True:
            myticket.append(l.strip())
            l=f.readline()
            yours=False

        elif other==True:
            others.append(l.strip())
            l=f.readline()
        elif 'your ticket' not in l and 'nearby' not in l:
            rules.append(l.strip())
            l=f.readline()
        elif 'your ticket' in l:
            yours=True
            l=f.readline()
        elif 'nearby' in l:
            other=True
            l=f.readline()
            



ranges=[]
for r in rules:
    tmp=(r.split(' '))
    rang1=[]
    for t in tmp:
        
        if '-' in t:
            ran=t.split('-')
            rang1.append((int(ran[0]),int(ran[1])))
    if rang1!=[]:
        ranges.append(rang1)

counter=0
removetick=[]
invalids=[]
for ticket in others:
    ticknums=ticket.split(',')
    for n in range(0,len(ticknums)):
        
        valid=False
        for r in ranges:
            rang1=r[0]
            rang2=r[1]
            r1=rang1[0]
            r2=rang1[1]
            r3=rang2[0]
            r4=rang2[1]
            if (int(ticknums[n]) >= r1 and int(ticknums[n]) <= r2) or (int(ticknums[n]) >= r3 and int(ticknums[n]) <= r4):
                valid=True
                
                break
        if valid==False:
            invalids.append(int(ticknums[n]))
            
            removetick.append(ticket)
            counter=counter+1
            break
for obj in removetick:
    others.remove(obj)


#part2
columns=[]

for i in range(0,20):
    c=[]
    for t in others:
        tmp=t.split(',')
        c.append(int(tmp[i]))
    columns.append(c)


table={}
for k in range(0,20):
    table[k]=set()
colcount=0

for col in columns:
    
    tip=0
    for x in col:
        rcount=0
        tip=tip+1
        for r in ranges:
            rang1=r[0]
            rang2=r[1]
            r1=rang1[0]
            r2=rang1[1]
            r3=rang2[0]
            r4=rang2[1]
            
            if (x<r1 or x>r2) and (x<r3 or x>r4):
                    
                    table[colcount].add(rcount) 
                    
            
            rcount+=1
    
            
    colcount+=1
    
#ranges 0-5 are departure
# i ran this block from 0 to 20 and wrote a table on paper
#worked out the values by hand, like sudoku
for k,v in table.items():
    if 12 in v:
        print(k)
#answer i got from paper working
myans=[5,1,8,2,15,11]
mine=myticket[0].split(',')
anssum=1
for n in range(len(mine)):
    if n in myans:
        anssum=anssum*int(mine[n])
print(anssum)



                
