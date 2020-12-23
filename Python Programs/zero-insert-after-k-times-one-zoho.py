Zero Insert After K Times One [ZOHO]
Given a bit stream of length N consisting of 0s and 1s, insert 0 after 1 has appeared K times consecutively.
Input Format:
The first line contains N and K separated by a space.
The second line contains the bit stream with 1s and 0s with each value separated by a space.
Output Format:
The first line the bit stream with the 0 inserted after 1s have appeared K times with each value separated by a space.
Boundary Conditions:
1 <= K <= 1000
2 <= N <= 1000
Example Input/Output 1:
Input:
12 2
1 0 1 1 0 1 1 0 1 1 1 1
Output:
1 0 1 1 0 0 1 1 0 0 1 1 0 1 1 0
a,b=map(int,input().split())
l=list(map(int,input().split()));c=0
for i in l:
    if i==1:c+=1;print(i,end=' ')
    else:c=0;print(i,end=' ')
    if c==b:print(0,end=' ');c=0
