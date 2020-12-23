Product of Current and Next Elements
Given an array of integers of size N as input, the program must print the product of current element and next element if the current element is greater than the next element. Else the program must print the current element without any modification.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N integers separated by space(s).
Example Input/Output 1:
Input:
6
5 4 6 5 7 2
Output:
20 4 30 5 14 2
Explanation:
For 1st element, 5>4 so the output is 5*4=20
For 2nd element, 4<6 so the output is 4
For 3rd element, 6>5 so the output is 6*5=30
For 4th element, 5<7 so the output is 5
For 5th element, 7>2 so the output is 14
For 6th element there is no next element, so the output is 2

Example Input/Output 2:
Input:
5
22 21 30 2 5
Output:
462 21 60 2 5
Explanation:
For 1st element, 22>21 so the output is 22*21=462
For 2nd element, 21<30 so the output is 21
For 3rd element, 30>2 so the output is 30*2=60
For 4th element, 2<5 so the output is 2
For 5th element there is no next element, so  the output is 5
n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if(l[i]>l[i+1]):
        print(l[i]*l[i+1],end=" ")
    else: 
        print(l[i],end=" ")
print(l[n-1])
