#get input
grid=[]

with open('day3input.txt') as f:
    l=f.readline()
    while l:
        tmp=[]
        for item in l:
            if item!='\n':
                tmp.append(item)
        grid.append(tmp)
        
        l=f.readline()


def trav(grid,right,down):
    startright=0
    count=0
    startdown=0
    while startdown<len(grid):
        if startright>=len(grid[0]):
            startright=startright-len(grid[0])
        r=grid[startdown][startright]
        
        if r=='#':
            count=count+1
        startdown=startdown+down
        startright=startright+right
    return(count)
tups=[(1,1),(3,1),(5,1),(7,1),(1,2)]
mul=1
for pair in tups:
    c=trav(grid,pair[0],pair[1])
    mul=mul*c
print(mul)
