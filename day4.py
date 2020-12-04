creds=['byr','iyr','eyr','hgt','hcl','ecl','pid']
eyecolours=['amb','blu','brn','gry','grn','hzl','oth']
tmp=[]
li=[]
valid=0
with open('day4input.txt') as f:
    l=f.readline()
    while l:
        
        if l=='\n':
            li.append(tmp)
            tmp=[]
        else:
            tmp.append(l)
        l=f.readline()
    li.append(tmp)
    tmp=[]
#each list in li is a passport
for passport in li:
    
    count=0
    for t in passport:
        c=t.split(' ')
        for fi in c:
            fields=fi.split(':')
            test=fields[0]
            test2=fields[1]
            if '\n' in test2:
                test2=test2[:-1]
            if test=='byr':
                if int(test2)>=1920 and int(test2)<=2002:
                    count=count+1
            elif test=='iyr':
                    if int(test2)>=2010 and int(test2)<=2020:
                        count=count+1
            elif test=='eyr':
                if int(test2)>=2020 and int(test2)<=2030:
                        count=count+1
            elif test=='hgt':
                if test2[len(test2)-2:]=='cm':
                    if int(test2[:len(test2)-2])>=150 and int(test2[:len(test2)-2])<=193:
                            count=count+1
                if test2[len(test2)-2:]=='in':
                    if int(test2[:len(test2)-2])>=59 and int(test2[:len(test2)-2])<=76:
                            count=count+1
            elif test=='hcl':
                if test2[0]=='#':
                    if len(test2)==7:
                        if test2[1:].isalnum():
                            count=count+1
            elif test=='ecl':
                if test2 in eyecolours:
                    count=count+1
            elif test=='pid':
                if test2.isnumeric():
                    if len(test2)==9:
                        count=count+1
            else:
                print('cid present')
    if count==len(creds):
        valid=valid+1
print(valid)
