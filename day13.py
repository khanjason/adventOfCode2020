n=0
li=[]
with open('day13input.txt') as f:
    n=int(f.readline().strip())
    l=f.readline().strip()
    li=l.split(',')
print(n)
#part1
buses=[]
for item in li:
    if item!='x':
        buses.append(int(item))

print(buses)

def getmax(n,bus):
    prev=0
    c=0
    while c<n:
        prev=c
        c=c+bus
    return c
    print(c)

times=[]
for b in buses:
    times.append(getmax(n,b))

m=min(times)
ind=times.index(m)
bus=buses[ind]

print(bus*(m-n))
#part2

sched=[]

for item in li:
    if item!='x':
        sched.append(int(item))
    else:
        sched.append(item)
print(sched)

#off set is index in sched
#find x

#start*x=offset mod bus
#chinese remainder theorem

offsets=[]
for b in buses:
    offsets.append(b-sched.index(b))
print(offsets)


#https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 

 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



print((chinese_remainder(buses, offsets)))


