Mirror Pattern - Ascending Descending Order
Accept an integer N as the input. The program must print the mirror pattern as shown in the Example Input/Output section below.
Boundary Condition(s):
2 <= N <= 50
Input Format:
The first line contains the value of N.
Output Format:
The first N*N lines contain the mirror pattern.
Example Input/Output 1:
Input:
3
Output:
1
23
456
654
32
1
Example Input/Output 2:
Input:
5
Output:
1
23
456
78910
1112131415
1514131211
10987
654
32
1
n=input().strip();n=int(n);s=2;c=1;k=1
for i in range(n):
    for j in range(1,s):
        print(c,end='');c+=1
    print('');s+=1
for i in range(n):
    for j in range(n-i):
        print(c-1,end='');c-=1 
    print('')
