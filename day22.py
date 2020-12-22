import heapq
player1=[]
player2=[]
playertwo=False
with open('day22input.txt') as f:
    l=f.readline()
    while l:
        if 'Player 1' in l:
            playertwo==False
        if 'Player 2' in l:
            playertwo=True
        if playertwo==False and 'Player' not in l:
            if l!='/n':
                tmp=l.strip()
                if tmp!='':
                    player1.append(int(tmp))
        if playertwo==True and 'Player' not in l:
            if l!='/n':
                tmp=l.strip()
                if tmp!='':
                    player2.append(int(tmp))
        l=f.readline()
player1=player1
player2=player2

#part1
def turn(heap1,heap2):
    
    p1=heap1[0]
    heap1=heap1[1:]
    p2=heap2[0]
    heap2=heap2[1:]
    
    pushlist=[]
    if p1>p2:
        pushlist.append(p1)
        pushlist.append(p2)
        heap1.append(pushlist[0])
        heap1.append(pushlist[1])
    elif p2>p1:
        pushlist.append(p2)
        pushlist.append(p1)
        heap2.append(pushlist[0])
        heap2.append(pushlist[1])
    
    return (heap1,heap2)
while player1!=[] and player2!=[]:
    r=turn(player1,player2)
    player1=r[0]
    player2=r[1]
tot=0

if len(player1)>len(player2):
    m=player1[::-1]
elif len(player1)<len(player2):
    m=player2[::-1]
for i in range(1,len(m)+1):
    
    tot=tot+(m[i-1]*i)
print(tot)

#part2
memo=[]

player1=[]
player2=[]
playertwo=False
with open('day22input.txt') as f:
    l=f.readline()
    while l:
        if 'Player 1' in l:
            playertwo==False
        if 'Player 2' in l:
            playertwo=True
        if playertwo==False and 'Player' not in l:
            if l!='/n':
                tmp=l.strip()
                if tmp!='':
                    player1.append(int(tmp))
        if playertwo==True and 'Player' not in l:
            if l!='/n':
                tmp=l.strip()
                if tmp!='':
                    player2.append(int(tmp))
        l=f.readline()
player1=player1
player2=player2


def turn2(heap1,heap2,memo):
    #print("player 1's deck: ",heap1)
    #print("player 2's deck: ",heap2)
    p1=heap1[0]
    heap1=heap1[1:]
    p2=heap2[0]
    heap2=heap2[1:]
    
    pushlist=[]
    t1=''.join(str(v) for v in heap1)
    t2=''.join(str(v) for v in heap2)
    
    if [t1,t2] in memo:
        #print('loop')  
        return(heap1,[])
    
    elif p1<=len(heap1) and p2<=len(heap2):
        t1=''.join(str(v) for v in heap1)
        t2=''.join(str(v) for v in heap2)
        
        #print("entering subgame")
        memo=[]
        
        st=recurs(p1,p2,heap1,heap2,memo)
        if st=='p1':
            pushlist.append(p1)
            pushlist.append(p2)
            heap1.append(pushlist[0])
            heap1.append(pushlist[1])
        elif st=='p2':
            pushlist.append(p2)
            pushlist.append(p1)
            heap2.append(pushlist[0])
            heap2.append(pushlist[1])
        return (heap1,heap2)
    elif p1>p2:
        t1=''.join(str(v) for v in heap1)
        t2=''.join(str(v) for v in heap2)
        memo.append([t1,t2])
        pushlist.append(p1)
        pushlist.append(p2)
        heap1.append(pushlist[0])
        heap1.append(pushlist[1])
        
    elif p2>p1:
        t1=''.join(str(v) for v in heap1)
        t2=''.join(str(v) for v in heap2)
        memo.append([t1,t2])
        pushlist.append(p2)
        pushlist.append(p1)
        heap2.append(pushlist[0])
        heap2.append(pushlist[1])
        #print("player 2 wins")
    return (heap1,heap2)

def recurs(val1,val2,heap1,heap2,memo):
    copy1=[]
    copy2=[]
    len1=len(heap1)
    len2=len(heap2)
    for item in range(0,val1):
        copy1.append(heap1[item])
    for i in range(0,val2):
        copy2.append(heap2[i])
    while copy1!=[] and copy2!=[]:
        r=turn2(copy1,copy2,memo)
        copy1=r[0]
        copy2=r[1]
    
    if copy1!=[]:
        #print("player 1 wins subgame")
        return "p1"
    else:
        #print("player 2 wins subgame")
        return "p2"
#this takes a few mins :(    
while player1!=[] and player2!=[]:
    r=turn2(player1,player2,memo)
    player1=r[0]
    player2=r[1]
tot=0

if len(player1)>len(player2):
    m=player1[::-1]
elif len(player1)<len(player2):
    m=player2[::-1]
for i in range(1,len(m)+1):
    
    tot=tot+(m[i-1]*i)
print(tot)

    
