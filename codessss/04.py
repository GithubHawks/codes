import operator
inp=[]
c_cnt=0
w_cnt=0
n=int(input())
for i in range(n):                                                   
    a,b=input().split()
    a=int(a)
    b=int(b)
    c_cnt=a
    w_cnt = c_cnt+b
    # print(c_cnt,w_cnt)
    l=int(w_cnt/7)
    fcnt=c_cnt+l
    inp.append(fcnt)
for i in inp:
    print(i)


    # x=[int(i) for i in input().split()]

    


