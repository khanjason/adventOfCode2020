


#left bag in dict with right bag#
#tuple of quantity and name
d=dict()
with open('day7input.txt') as f:
    line=f.readline()
    while line:
            s=line.split('contain')
            bag=s[1].strip()#split(',')
            b=bag.split(',')
            second=[]
            for item in b:
                    t=item.strip()
                    t=t.replace('bags','bag')
                    t=t.replace('.','')
                    num=t[0]
                    name=t[1:].strip()
                    second.append((num,name))
            first=s[0].replace('bags','bag')
            d[first.strip()]=second
            line=f.readline()


#traverse function which takes in a target e..g shiny gold bag and outputs single routes
#run traverse until key not found
#part 1
            s=set()
def traverse(target,tree,se):
    bagsfound=[]
    for k,v in tree.items():
        
        for item in v:
            for t in target:
                if(item[1]==t):
                    bagsfound.append(k)
                    s.add(k)
    return bagsfound
start=['shiny gold bag']

while start!=[]:
    start=traverse(start,d,s)
print(len(s))


#part 2
tot=1
def traverse2(t,tree):
    if t in d.keys():
        
        print(d[t])
    else:
        return -1

