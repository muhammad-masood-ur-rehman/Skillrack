Sum of Matrices - Reverse Rows
The program must accept two integer matrices M1 and M2 are of equal size RxC as the input. In M1 and M2, The program must reverse the integers in the odd positions of the odd rows and the integers in the even positions of the even rows. Then the program must print the sum of M1 and M2 as the output.

Example Input/Output 1:
Input:
5 5
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
9 3 5 6 9
4 2 8 7 6
8 6 5 9 2
4 6 2 8 1
1 6 3 4 5

Output:
14 5 8 10 10
6 12 12 5 12
9 10 10 15 11
8 15 8 11 9
14 12 10 12 6

Example Input/Output 2:
Input:
2 6
50 81 56 50 58 56
68 16 17 56 84 49
20 88 36 20 81 36
83 44 16 26 86 92
Output:
139 169 92 70 70 92
151 141 33 82 170 60
def rev(x,a,b):
  c=[]
  for i in range(a):
    p=[];f=[];d=[]
    if i%2==0:
      for j in range(b):
        if j%2==0:
            p.append(x[i][j])
            f.append(j)
      p=p[::-1]
      l=0
      for h in range(b):
        if l<len(p) and h==f[l]:
            d.append(p[l])
            l+=1
        else:
            d.append(x[i][h])
      c.append(d)
    else:
      for j in range(b):
        if j%2!=0:
            p.append(x[i][j])
            f.append(j)
      p=p[::-1];l=0
      for h in range(b):
        if l<len(p) and h==f[l]:
            d.append(p[l])
            l+=1
        else:
            d.append(x[i][h])
      c.append(d)
  return c
a,b=map(int,input().split())
l=[input().split() for i in range(a)]
y=[input().split() for i in range(a)]
m=rev(l,a,b);n=rev(y,a,b)
for i in range(a):
  for j in range(b):
      print(int(m[i][j])+int(n[i][j]),end=' ')
  print()
