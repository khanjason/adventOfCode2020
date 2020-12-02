#part1
count=0
with open('day2input.txt') as f:
    
    l=f.readline()
    while l:
        li=l.split(' ')
        t=li[1][0]
        password=li[2]
        rangelist=li[0].split('-')
        begin=int(rangelist[0])
        end=int(rangelist[1])
        if password.count(t)>=begin:
            if password.count(t)<=end:
                count=count+1
        l=f.readline()
print(count)
#part2
count=0
with open('day2input.txt') as f:
    
    l=f.readline()
    while l:
        li=l.split(' ')
        t=li[1][0]
        password=li[2]
        rangelist=li[0].split('-')
        ind1=int(rangelist[0])-1
        ind2=int(rangelist[1])-1
        if password[ind1]==t:
            if password[ind2]!=t:
                count=count+1
        elif password[ind2]==t:
            if password[ind1]!=t:
                count=count+1
        l=f.readline()
print(count)
