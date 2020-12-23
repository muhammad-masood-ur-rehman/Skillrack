Sort Between Multiples
Sort Between Multiples: The program must accept N integers and an integer X as the input. The program must sort the integers present between consecutive multiples of X in ascending order. Then the program must print the sorted integers as the output.
Boundary Condition(s):
1 <= N, X <= 1000
Input Format:
The first line contains N and X separated by a space.
The second line contains N integers separated by a space.
Output Format:
The first line contains N integers separated by a space.
Example Input/Output 1:
Input:
7 2
2 5 3 12 13 9 8
Output:
2 3 5 12 9 13 8
Explanation:
The integers present between the multiples of 2 (2 and 12) are 5 and 3 which are sorted.
The Next set of integers present between the multiples of 2 (12 and 8) are 13 and 9 which are sorted.
Example Input/Output 2:
Input:
10 4
38 22 52 40 64 46 5 29 60 90
Output:
38 22 52 40 64 5 29 46 60 90
n,x=map(int,input().split())
l=list(map(int,input().split()));c=0;k=[];p=[];a=[]
for i in range(n):
  if l[i]%x!=0 and c==0 and l[i] not in a:a.append(l[i])
  elif l[i]%x==0:c+=1;k.append(i)
  else:p.append(l[i]) 
  f=0
  if c==2:
    for i in range(2):
      if l[k[i]] not in a:a.append(l[k[i]])
      if  f==0:
        for u in sorted(p):a.append(u)
        f=1
    c=1;k=k[1:];p=[]
print(*(a+p))
