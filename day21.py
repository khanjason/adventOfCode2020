li=[]
tmp=[]
ingreds=[]
with open('day21input.txt') as f:
    l=f.readline()
    while l:
        if '(' in l:
            half=l.split('(')
            tmp=tmp+half[0].split(' ')
            ing=half[1].strip().split(', ')
            for g in range(len(ing)):
                if 'contains' in ing[g]:
                    ing[g]=ing[g][9:]
                if ')' in ing[g]:
                    ing[g]=ing[g][:len(ing[g])-1]
            ingreds.append(ing)
            for item in tmp:
                if item=='':
                    tmp.remove(item)
            li.append(tmp)
            tmp=[]
        else:
            tmp=tmp+l.split(' ')
        l=f.readline()
print(li)
print(ingreds)
