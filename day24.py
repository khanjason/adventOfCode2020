instruct=[]
#each line is like a movement instruction
#each tile is coordinate
#count the number of cordinates encoutnered
s=set()
with open('day24input.txt') as f:
    l=f.readline()
    while l:
        instruct.append(l.strip())
        l=f.readline()

ins=[]
#part1
def converttohash(coords):
    t=''
    for item in coords:
        t=t+str(item)
        t=t+','
    return t
def unhash(hashh):
    t=[]
    tmp=hashh.split(',')
    for item in tmp:
        if item!='':
            t.append(int(item))
    return t
        

for i in instruct:
    conn=False
    tmp=[]
    t=''
    for c in i:
        if conn==True:
            t=t+c
            tmp.append(t)
            t=''
            conn=False
        elif c=='n' or c=='s':
            conn=True
            t=t+c
        else:
            tmp.append(c)
    ins.append(tmp)
  

for tile in ins:
    config=[0,0]
    for i in tile:
        if i=='se':
            
            config[0]+=1
        if i=='nw':
            config[0]-=1
        if i=='sw':
            config[1]-=1
            config[0]+=1
        if i=='ne':
            config[1]+=1
            config[0]-=1
        if i=='e' :
            config[1]+=1
        if i=='w' :
            config[1]-=1
    tryy=converttohash(config)
    if tryy in s:
        s.remove(tryy)
    else:
        s.add(tryy)

print(len(s))
#part2


maxy=0
maxx=0

def getneighbours(coords):
    neigh=[]
    neigh.append([coords[0],coords[1]+1])
    neigh.append([coords[0],coords[1]-1])
    neigh.append([coords[0]+1,coords[1]])
    neigh.append([coords[0]-1,coords[1]])
    neigh.append([coords[0]+1,coords[1]-1])
    neigh.append([coords[0]-1,coords[1]+1])
    return neigh
def turn(tiles):
    safety=set()
    #start with black
    for c in tiles:
        coord=unhash(c)
        neighbs=getneighbours(coord)
        count=0
        for n in neighbs:
            if converttohash(n) in tiles:
                count=count+1
        if count!=0 and count<3:
            safety.add(converttohash(coord))
    for co in tiles:
        coord=unhash(co)
        neighbs=getneighbours(coord)
        count=0
        for n in neighbs:
            if converttohash(n) not in tiles:
                count=0
                nei=getneighbours(n)
                for ne in nei:
                    if converttohash(ne) in tiles:
                        count=count+1
                if count==2:
                    safety.add(converttohash(n))
    return safety

for t in range(0,100):
    s=turn(s)
print(len(s))
