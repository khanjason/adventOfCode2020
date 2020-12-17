li=[]
with open('day17input.txt') as f:
    l=f.readline()
    while l:
        li.append(l.strip())
        l=f.readline()


class slot():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.neighbours=[]
        self.val='.'
    def getneighbours(self):
        self.neighbours.append([x+1,y,z])
        self.neighbours.append([x-1,y,z])
        self.neighbours.append([x,y+1,z])
        self.neighbours.append([x,y-1,z])
        self.neighbours.append([x,y,z+1])
        self.neighbours.append([x,y,z-1])
        #doubles
        self.neighbours.append([x+1,y+1,z])
        self.neighbours.append([x+1,y-1,z])
        self.neighbours.append([x-1,y-1,z])
        self.neighbours.append([x,y+1,z+1])
        self.neighbours.append([x,y-1,z-1])
        self.neighbours.append([x,y+1,z-1])
        self.neighbours.append([x,y-1,z+1])
        self.neighbours.append([x-1,y+1,z])
        self.neighbours.append([x+1,y,z+1])
        self.neighbours.append([x+1,y,z-1])
        self.neighbours.append([x-1,y,z+1])
        self.neighbours.append([x-1,y,z-1])
        #tiples
        self.neighbours.append([x-1,y-1,z-1])
        self.neighbours.append([x+1,y+1,z+1])
        self.neighbours.append([x-1,y+1,z+1])
        self.neighbours.append([x-1,y+1,z-1])
        self.neighbours.append([x-1,y+1,z+1])
        self.neighbours.append([x+1,y-1,z-1])
        self.neighbours.append([x+1,y+1,z-1])
        self.neighbours.append([x+1,y-1,z+1])
    def setval(self,v):
        self.val=v
        
        
        
        
                
        
        
        
        
s=[]
for r in range(len(li)):
    for y in range(len(li[r])):
        n=slot(r,y,0)
        n.setval(li[r][y])
        s.append(n)
for cube in s:
    print(cube.x,cube.y,cube.z,cube.val)
