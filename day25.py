#public key
#find loop size
#find initial subject

#start with 1
#loop
#set value to itself mutiplitied by the subject number
#set value to remainder after % 20201227


#transform 7 using card to get card public key
#transform 7 using door to get door public key
#puzzle input are both public keys
#card transforms subject number door public key using card loop
#door transforms subject number of the cards public key according to door loop size
#encryption key is the same

subject=7
public_keys=[10212254,12577395]
target=public_keys[0]
encrypts=[]
loops=[]
loop=0
val=1
while val!=target:
    loop+=1
    val=val*subject
    val=val%20201227
loops.append(loop)
target=public_keys[1]
loop=0
val=1
while val!=target:
    loop+=1
    val=val*subject
    val=val%20201227
loops.append(loop)
print(loops)
val=1
subject=public_keys[1]
for i in range(0,loops[0]):
    val=val*subject
    val=val%20201227
encrypts.append(val)

val=1
subject=public_keys[0]
for t in range(0,loops[1]):
    val=val*subject
    val=val%20201227
encrypts.append(val)
print(encrypts)
