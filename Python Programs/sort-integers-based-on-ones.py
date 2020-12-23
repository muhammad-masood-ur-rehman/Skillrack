Sort Integers based on Ones
The program must accept N integers as the input. The program must sort the integers based on the number of ones in their binary representation in descending order. If more than one integers have the same number of ones in their binary representation, the program must sort those integers in ascending order. Finally, the program must print the N sorted integers as the output.
Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^8
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first line contains the N sorted integers separated by a space.
Example Input/Output 1:
Input:
6
65 2 78 790 10 31
Output:
31 790 78 10 65 2
Explanation:
The binary representation of 31 is 11111.
The binary representation of 790 is 1100010110.
The binary representation of 78 is 1001110.
The binary representation of 10 is 1010.
The binary representation of 65 is 1000001.
The binary representation of 2 is 10.
Here the 6 integers are sorted based on the number of ones in their binary representation.
Example Input/Output 2:
Input:
5
9 15 6 4 14
Output:
15 14 6 9 4
n=int(input())
a=list(map(int,input().split()))
l,k=[],[]
for i in a:
    b=bin(i)[2:]
    l.append([b.count("1"),i])
    if b.count("1") not in k:
        k.append(b.count("1"))
l.sort()
k.sort(reverse=True)
i=n-1
while(i>-1):
    j=i-1
    m=[]
    m.append(l[i][1])
    while(j>=0 and l[i][0]==l[j][0]):
        m.append(l[j][1])
        j=j-1
    print(*m[::-1],end=" ")
    i=j
