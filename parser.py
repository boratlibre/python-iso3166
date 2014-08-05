# Antarctica and last few lines of null, null regions are removed
# Changed Korea, Democratic People's Republic of to North Korea
# Changed Korea, Republic of to South Korea
f=open('raw-data.txt')
for l in f:
    l=l.replace("\n","")
    comma=l.find(",")
    if comma>0:
        l=l[:comma]

    parts=l.split(" ")
    while(len(parts[3])<3):
        parts[3]="0"+parts[3]
    while len(parts)>5:
        parts[4]+=" " +parts[5]
        del parts[5]

    print 'Country(u"%s","%s","%s","%s","%s"),' % (parts[4],parts[1],parts[2],parts[3],parts[0])