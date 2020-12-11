#game of life
#make a passer
li=[]
with open('day11input.txt') as f:
    l=f.readline()
    while l:
        tmp=[]
        for item in l.strip():
            tmp.append(item)
        li.append(tmp)
        l=f.readline()


def display(lis):
    for row in lis:
        print(row)
#display(li)

def getadjacencies(lis,row,seat):
    t=[]
    if seat==0 and row==0: #top left corner
        t.append(lis[row][seat+1])#right
        t.append(lis[row+1][seat])#down
        t.append(lis[row+1][seat+1])#bottom right
        return t

    elif row==0 and seat==len(lis[row])-1: #top right
        t.append(lis[row+1][seat-1])#bottom left
        t.append(lis[row][seat-1])#left
        t.append(lis[row+1][seat])#down
        return t
    elif row==len(lis)-1 and seat==0: #bottom left corner
        
        t.append(lis[row-1][seat])#up
        t.append(lis[row][seat+1])#right
        t.append(lis[row-1][seat+1])#upper right
        return t

    elif row==len(lis)-1 and seat==len(lis[row])-1: #bottom right  corner
        
        t.append(lis[row-1][seat])#up
        t.append(lis[row][seat-1])#left
        t.append(lis[row-1][seat-1])#upper left
        return t
        
    elif row==0: #top
        t.append(lis[row+1][seat])#down
        t.append(lis[row+1][seat+1])#bottom right
        t.append(lis[row+1][seat-1])#bottom left
        t.append(lis[row][seat-1])#left
        t.append(lis[row][seat+1])#right
        return t


    elif row==len(lis)-1: #bottom
        t.append(lis[row-1][seat])#up
        t.append(lis[row-1][seat-1])#upper left
        t.append(lis[row-1][seat+1])#upper right
        t.append(lis[row][seat-1])#left
        t.append(lis[row][seat+1])#right
        return t
        
    elif seat==0:#first
        t.append(lis[row][seat+1])#right
        t.append(lis[row+1][seat+1])#bottom right
        t.append(lis[row+1][seat])#down
        t.append(lis[row-1][seat])#up
        
        t.append(lis[row-1][seat+1])#upper right
        return t
        
    elif seat==len(lis[row])-1: #last
        t.append(lis[row][seat-1])#left
        t.append(lis[row+1][seat])#down
        t.append(lis[row+1][seat-1])#bottom left
        t.append(lis[row-1][seat])#up
        t.append(lis[row-1][seat-1])#upper left
        return t
    else:
        
        t.append(lis[row][seat+1])#right
        t.append(lis[row+1][seat+1])#bottom right
        t.append(lis[row+1][seat-1])#bottom left
        t.append(lis[row][seat-1])#left
        t.append(lis[row+1][seat])#down
        t.append(lis[row-1][seat])#up
        t.append(lis[row-1][seat-1])#upper left
        t.append(lis[row-1][seat+1])#upper right
        
    
        return t
    return t

def copy(li):
    t=[]
    for item in li:
        p=[]
        for i in item:
            p.append(i)
        t.append(p)
    return t

def passstep(lis,row,seat):
    if lis[row][seat]=='L':
        r=getadjacencies(lis,row,seat)
                
        if r.count('#')==0:
            #cop[row][seat]='#'
            #print(r)
            return 0
        return -1
    elif lis[row][seat]=='#':
        r=getadjacencies(lis,row,seat)
                
        if r.count('#')>=4:
            #cop[row][seat]='L'
            
            return 1
        return -1
    else:
        return -1

#part1
def passer(lis):
    cop=copy(lis)
    change=False
    
    for row in range(0,len(lis)):
        for seat in range(0,len(lis[0])):

            n=passstep(lis,row,seat)
            if n==0:
                cop[row][seat]='#'
                change=True
            elif n==1:
                cop[row][seat]='L'
                change=True
            
    
    return [cop,change]

def counting(lis,char):
    count=0
    for t in lis:
        for c in t:
            #print(t)
            if c==char:
                count=count+1
    return count

print('num of rows: ',len(li)-1)#number of rows
print('num of seats per row: ',len(li[0])-1) #number of seats
change=True
count=0
start=copy(li)

while change:
    r=passer(start)
    start=r[0]
    change=r[1]
    count+=1
    
    
print('number occupied: ',counting(start,'#'))

print('passes: ',count)

print(counting(start,'#'))


#part2



def getvisible(lis,row,seat):
    t=[]
    #top left corner
    if row==0 and seat==0:
        #pass towards the right
        
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break

        #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break

        #pass diagonal - bottom right
        leftp=seat+1
        upp=row+1
        while leftp!=len(lis[row]) and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp+=1
        return t
    #top right corner
    elif row==0 and seat==len(lis[row])-1:
        
        #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        
        #pass diagonal - bottom left
        leftp=seat-1
        upp=row+1
        while leftp!=-1 and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp+=1
        return t
    #bottom right corner
    elif row==len(lis)-1 and seat==len(lis[row])-1:
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break
        #pass diagonal - top left
        leftp=seat-1
        upp=row-1
        while leftp!=-1 and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp-=1
        return t
    #bottom left corner
    elif row==len(lis)-1 and seat==0:
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break
        #pass towards the right
        
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass diagonal - top right
        
        leftp=seat+1
        upp=row-1
        while leftp!=len(lis[row]) and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp-=1
        return t
    #top row
    elif row==0:
         #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass towards the right
        
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass diagonal - bottom left
        leftp=seat-1
        upp=row+1
        while leftp!=-1 and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp+=1
        #pass diagonal - bottom right
        leftp=seat+1
        upp=row+1
        while leftp!=len(lis[row]) and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp+=1
        return t
    #bottom
    elif row==len(lis)-1:
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass towards the right
        
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break
        #pass diagonal - top left
        leftp=seat-1
        upp=row-1
        while leftp!=-1 and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp-=1
        #pass diagonal - top right
        
        leftp=seat+1
        upp=row-1
        while leftp!=len(lis[row]) and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp-=1
        return t

    #first column
    elif seat==0:
        #pass towards the right
        
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break

        #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break
        #pass diagonal - top right
        
        leftp=seat+1
        upp=row-1
        while leftp!=len(lis[row]) and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp-=1

        #pass diagonal - bottom right
        leftp=seat+1
        upp=row+1
        while leftp!=len(lis[row]) and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp+=1
        return t
    #right
    elif seat==len(lis[row])-1:
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break

        #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break
        #pass diagonal - top left
        leftp=seat-1
        upp=row-1
        while leftp!=-1 and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp-=1
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass diagonal - bottom left
        leftp=seat-1
        upp=row+1
        while leftp!=-1 and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp+=1
        return t
    else:
        #pass towards the left
        for i in range(seat-1,-1,-1):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        
        #pass towards the right
            
        for i in range(seat+1,len(lis[row])):
            if lis[row][i]!='.':
                t.append(lis[row][i])
                break
        #pass upwards
        for i in range(row-1,-1,-1):
            if lis[i][seat]!='.':
                t.append(lis[i][seat])
                break

        #pass downwards
        for n in range(row+1,len(lis)):
            if lis[n][seat]!='.':
                t.append(lis[n][seat])
                break
        #pass diagonal - top left
        leftp=seat-1
        upp=row-1
        while leftp!=-1 and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp-=1
        #pass diagonal - top right
            
        leftp=seat+1
        upp=row-1
        while leftp!=len(lis[row]) and upp!=-1:
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp-=1
        #pass diagonal - bottom left
        leftp=seat-1
        upp=row+1
        while leftp!=-1 and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp-=1
            upp+=1
        #pass diagonal - bottom right
        leftp=seat+1
        upp=row+1
        
        while leftp!=len(lis[row]) and upp!=len(lis):
            if lis[upp][leftp]!='.':
                t.append(lis[upp][leftp])
                break
            leftp+=1
            upp+=1
        return t
def passstep2(lis,row,seat):
    if lis[row][seat]=='L':
        r=getvisible(lis,row,seat)
                
        if r.count('#')==0:
            
            return 0
        return -1
    elif lis[row][seat]=='#':
        r=getvisible(lis,row,seat)
                
        if r.count('#')>=5:
            
            
            return 1
        return -1
    else:
        return -1

#part2
li=[]
with open('day11input.txt') as f:
    l=f.readline()
    while l:
        tmp=[]
        for item in l.strip():
            tmp.append(item)
        li.append(tmp)
        l=f.readline()


def passer2(lis):
    cop=copy(lis)
    change=False
    
    for row in range(0,len(lis)):
        for seat in range(0,len(lis[0])):

            n=passstep2(lis,row,seat)
            if n==0:
                cop[row][seat]='#'
                change=True
            elif n==1:
                cop[row][seat]='L'
                change=True
            
    
    return [cop,change]
change=True
count=0
start2=copy(li)

while change:
    r=passer2(start2)
    start2=r[0]
    change=r[1]
    count+=1
    
    
print('number occupied: ',counting(start2,'#'))

print('passes: ',count)

print(counting(start2,'#'))

