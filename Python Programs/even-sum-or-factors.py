Even Sum or Factors
The program must accept two integers M and N as the input. If M is even then the program must print the integers from 1 to N whose sum of the last two digits is even. Else the program must print all the integers from 1 to N having even number of factors as the output.
Boundary Condition(s):
1 <= M, N <= 10^4
Input Format:
The first line contains M and N separated by a space.
Output Format:
The first line contains integers separated by a space.
Example Input/Output 1:
Input:
3 15
Output:
2 3 5 6 7 8 10 11 12 13 14 15
Explanation:
The printed integers have even number of factors in it.
Example Input/Output 2:
Input:
6 50
Output:
2 4 6 8 11 13 15 17 19 20 22 24 26 28 31 33 35 37 39 40 42 44 46 48
Explanation:
The sum of the last two digits of the printed values are even.
m,n=map(int,input().split())
if m%2==0:
    for i in range(1,n+1):
        if(len(str(i))==1 and i%2==0)or(len(str(i))>1 and(int(str(i)[-1])+int(str(i)[-2]))%2==0):
            print(i,end=' ')
else:
    for i in range(1,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c%2==0:
            print(i,end=' ')
