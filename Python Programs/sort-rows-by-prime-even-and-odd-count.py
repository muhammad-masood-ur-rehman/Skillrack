Sort Rows by Prime, Even and Odd count
Sort Rows by Prime, Even and Odd count: An integer matrix of size R*C is given as input. The program must sort the rows based on the number of prime numbers in descending order. If two rows contain the same number of prime numbers then sort the rows based on the number of even numbers (also non-prime). If two rows contain the same number of prime numbers and the same number of even numbers then sort the rows based on the number of odd numbers (also non-prime). If two rows contain the same number of prime numbers, even numbers and odd numbers then sort the rows based on the sum of elements of each row in descending order.
Boundary Condition(s):
1 <= R, C <= 100
Input Format:
The first line contains R and C separated by space(s).
Next R lines contain C integers each separated by space(s).
Output Format:
R lines containing C integers with the rows sorted based on given conditions.
Example Input/Output 1:
Input:
5 5
4 6 4 3 1
3 1 1 5 3
1 7 2 3 3
3 2 6 9 8
1 4 3 7 4
Output:
1 7 2 3 3
3 1 1 5 3
3 2 6 9 8
1 4 3 7 4
4 6 4 3 1

Example Input/Output 2:
Input:
4 4
2 1 2 3
3 4 1 2
9 7 9 3
7 4 2 3 
Output:
7 4 2 3
2 1 2 3
3 4 1 2
9 7 9 3
import math
def prime(ab):
    f=0  
    if(ab<2):
        return 0
    for i in range(2,int(math.sqrt(ab))+1):
        if(ab%i==0):
            f=1 
            break 
    if(f==0):
        return 1 
    else:
        return 0
a,b=map(int,input().split()) 
c=[list(map(int,input().split())) for i in range(a)]  
d=[] 
iterator=0
for i in c:  
    pcount=0 
    ecount=0 
    ocount=0
    for j in i:
        if(prime(j)==1):
            pcount+=1   
        if(j%2!=0):
            ocount+=1 
        if(j%2==0):
            ecount+=1 
    d.append([pcount,ecount,ocount,sum(i),i]) 
    iterator+=1
d=sorted(d,reverse=True) 
for i in d:
    print(*i[4])
