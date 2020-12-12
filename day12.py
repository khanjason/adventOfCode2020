instruct=[]
with open('day12input.txt') as f:
    l=f.readline()
    while l:
        instruct.append(l.strip())
        l=f.readline()
#print(instruct)

#posx and posy which record relative distance at each instruction
#also 'current face'
#part1
def move(posx,posy,currentFace,action,value):
    #return [posx,posy,currentFace]
    order=['N','E','S','W'] #clockwise
    counterorder=['N','W','S','E'] #anticlockwise
    if action=='N':
        posy=posy+value
        
        return [posx,posy,currentFace]
    elif action=='S':
        posy=posy-value
        return [posx,posy,currentFace]
    
    elif action=='E':
        posx=posx+value
        return [posx,posy,currentFace]
    elif action=='W':
        posx=posx-value
        return [posx,posy,currentFace]
    
    
    elif action=='R':
        times=value//90
        start=order.index(currentFace)
        newind=start+times
        
        if newind>3:
            newind=newind-4
        currentFace=order[newind]
        
        return [posx,posy,currentFace]
    elif action=='L':
        times=value//90
        start=counterorder.index(currentFace)
        newind=start+times
        if newind>3:
            newind=newind-4
        currentFace=counterorder[newind]
        
        return [posx,posy,currentFace]
    elif action=='F':
        if currentFace=='N':
            posy=posy+value
            return [posx,posy,currentFace]
        elif currentFace=='S':
            posy=posy-value
            return [posx,posy,currentFace]
        
        elif currentFace=='E':
            posx=posx+value
            
            return [posx,posy,currentFace]
        elif currentFace=='W':
            posx=posx-value
            return [posx,posy,currentFace]
            

    else:
        print('invalid')
            
        
currentFace='E'
posx=0
posy=0

for obj in instruct:
    ac=obj[0]
    v=int(obj[1:])
    r=move(posx,posy,currentFace,ac,v)
    posx=r[0]
    posy=r[1]
    currentFace=r[2]
print(posx,posy,currentFace)
print(abs(posx)+abs(posy))
#part2


def move2(posx,posy,currentFace,action,value,shipx,shipy,waypointFace):
    #return [posx,posy,currentFace]
    order=['N','E','S','W'] #clockwise
    counterorder=['N','W','S','E'] #anticlockwise

    #stays the same
    if action=='N':
        posy=posy+value
        
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    elif action=='S':
        posy=posy-value
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    
    elif action=='E':
        posx=posx+value
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    elif action=='W':
        posx=posx-value
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    
    #change waypointFace
    elif action=='R':
        times=value//90
        startx=posx
        starty=posy
        if times==1:
            posy=-startx
            posx=starty
        elif times==2:
            posx=-startx
            posy=-starty
        elif times==3:
            posx=-starty
            posy=startx
        
        
        
        
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    elif action=='L':
        times=value//90
        startx=posx
        starty=posy
        if times==3:
            posy=-startx
            posx=starty
        elif times==2:
            posx=-startx
            posy=-starty
        elif times==1:
            posx=-starty
            posy=startx
        
        return [posx,posy,currentFace,shipx,shipy,waypointFace]

    #move towards waypointFAce
    #value is waypointx * val and waypoint y*val
    elif action=='F':
        
        valy=value*posy
        shipy=shipy+valy
        valx=value*posx
        shipx=shipx+valx
           
        
        return [posx,posy,currentFace,shipx,shipy,waypointFace]
    else:
        print('invalid')
            
#pos x and posy are waypoint's coords
#shipx and shipy
#waypointFace
currentFace='E'
waypointFace='E'
shipx=0
shipy=0
posx=10
posy=1

for obj in instruct:
    ac=obj[0]
    v=int(obj[1:])
    r=move2(posx,posy,currentFace,ac,v,shipx,shipy,waypointFace)
    posx=r[0]
    posy=r[1]
    currentFace=r[2]
    shipx=r[3]
    shipy=r[4]
    waypointFace=r[5]

print(abs(shipx)+abs(shipy))
