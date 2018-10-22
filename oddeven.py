name = input("Enter a fl st: ")
file = open(name+".txt",'r')
d = dict()
tup=[]
for lines in file:
    if lines.startswith("From:") :
        l=lines.split(": ")
        if l[1] not in d:
            d[l[1]]=1
        else:
            d[l[1]]=d[l[1]]+1
for i in d:
    tup.append((d[i],i))
sort=sorted(tup,reverse=True)

max=sort[0]
print("The maximum",max[0]," emails were sent by",max[1])
