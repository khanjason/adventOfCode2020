#list of sets
#part1
li=[]
counts=0
with open ('day6input.txt') as f:
    l=f.readline()
    tmp=set()
    while l:
        
        if l=='\n':
            li.append(tmp)
            counts=counts+len(tmp)
            tmp=set()
        else:
            for item in l:
                if item!='\n':
                    tmp.add(item)
        l=f.readline()
    li.append(tmp)
    counts=counts+len(tmp)
    tmp=set()
print(counts)
            
        
#part2
#each lein should be a set
#at each \n take the intersection of these sets and count length
li=[]
counts=0
with open ('day6input.txt') as f:
    l=f.readline()
    tmp=set()
    while l:
        if l=='\n':
            inter = set.intersection(*li)
            counts=counts+len(inter)
            li=[]
        else:
            for item in l:
                if item!='\n':
                    tmp.add(item)
            li.append(tmp)
        
        tmp=set()
        l=f.readline()
    inter = set.intersection(*li)
    counts=counts+len(inter)
    li=[]
print(counts)
            
