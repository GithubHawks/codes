a= []
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([score, name])
name=[]
a.sort()
print(a)
if a[0][0]!=a[1][0] and a[1][0]!=a[2][0]:
	b=a[2][0]
else:
	b=a[1][0]

for i in range(1,len(a)):
	if a[i][0]==a[1][0]:
		name.append(a[i][1])

name.sort()
for i in range(0,len(name)):
	print(name[i])

