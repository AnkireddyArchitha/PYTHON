bname=input("Enter boy name without spaces:")
gname=input("Enter girl name without spaces:")
l1=list(bname)
l2=list(gname)
for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            l1[i]='2'
            l2[j]='2'
print(l1)
print(l2)
x=sum(1 for i in l1 if i!='2')
y=sum(1 for j in l2 if j!='2')
print(x)
print(y)
count=x+y
ans=['F','L','A','M','E','S']
i=0
while(len(ans)!=1):
    i=(i+(count-1))%len(ans)
    ans.pop(i)
print(ans)
