import itertools
a,b = input().split(",")
a=int(a)#10
b=int(b)#2
spl_list=[]
fcnt=0
#lol dummyyyy
numbers = [i for i in range(1,a+1)]
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == a]
for i in range(len(result)):
	for j in range(len(result[i])-1):
		if result[i][j+1]-result[i][j]<b:
			break
	else:
		spl_list.append(result[i])

del spl_list[len(spl_list)-1]
spl_list
for i in range(len(spl_list)):
	cnt=0
	for j in range(len(spl_list[i])):
		if spl_list[i][j]%2==0 or spl_list[i][j]%3==0:
			cnt+=1
	if cnt>=2:
		fcnt+=1
print(fcnt)

