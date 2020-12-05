#128 rows
rows=[]
for i in range(0,128):
    rows.append(i)

#8 columns
columns=[]
for c in range(0,8):
    columns.append(c)

seats=[]
with open('day5input.txt') as f:
    l=f.readline()
    while l:
        if '\n' in l:
            l=l[:-1]
        seats.append(l)
        l=f.readline()

#for seat in seat get r and c in bin search
def binsearchrows(seat,section,lower,upper):
    
    for char in seat:
        
        mid=int(len(section)/2)
        if char==lower:
            
            section=section[:mid]
        if char==upper:
            
            section=section[mid:]
    return(section)

def getall():
    #1-126
    #output second set
    rows=[]
    sec=set()
    for i in range(1,126):
        rows.append(i)
    for r in rows:
        for col in columns:
            sec.add((r*8) + col)
    

    return sec
#testseat='FBFBBFFRLR'
m=set()
for testseat in seats:
    rcount=binsearchrows(testseat[:-3],rows,'F','B')[0]
    ccount=binsearchrows(testseat[-3:],columns,'L','R')[0]
    
    m.add((rcount*8) + ccount)

g=getall()
print(g.symmetric_difference(m))
