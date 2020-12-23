Water Image Pattern with Base
Water Image Pattern with Base: The program must accept two integers N and M as the input. The program must print the desired pattern as shown in the Example Input/Output sections.
Boundary Condition(s):
1 <= N,M <= 100
Input Format:
The first line contains the values of N and M.
Output Format:
The first Mx2 lines contain the desired pattern as shown in the Example Input/Output sections.
Example Input/Output 1:
Input:
3 4
Output:
3
44
555
6666
6666
555
44
3
Example Input/Output 2:
Input:
2 5
Output:
2
33
444
5555
66666
66666
5555
444
33
2
a,b=map(int,input().split())
for i in range(1,b+1):
    print(str(a)*i)
    a+=1
a-=1
for i in range(b,0,-1):
    print(str(a)*i)
    a-=1
a,b=map(int,input().split())
c=b-a+1;k=a;l=[]
for i in range(b):
   m=[]
   for j in range(i+1):
       m.append(k)
   k+=1
   l.append(m)
for i in l:
    print(*i,sep='')
for i in l[::-1]:
    print(*i,sep='')
