Largest & Smallest Unit Digit Numbers Difference
Largest & Smallest Unit Digit Numbers Difference: Given N numbers, the program must find and print the difference between numbers having the largest and smallest unit digits.
- If multiple numbers have the largest unit digit, then choose the largest number among them.
- If multiple numbers have the smallest unit digit, then choose the smallest number among them.
Input Format:
The first line contains N.
The second line contains N positive integers separated by a space.
Output Format:
The first line contains the difference between the numbers having the largest and smallest unit digits.
Boundary Conditions:
1 <= N <= 9999
Example Input/Output 1:
Input:
5
19 21 32 41 89
Output:
68
Explanation:
Two numbers 19 and 89 have the largest unit digit 9. We choose 89 as per the condition given.
Two numbers, 21 and 41 have the smallest unit digit 1. We choose 21 as per the condition given.
Hence the difference is 89-21 = 68
n=int(input());x=[];y=[]
l=list(map(int,input().split()))
k=[i%10 for i in l];ma=max(k);mi=min(k)
for i in l:
    if i%10==ma:x.append(i)
    if i%10==mi:y.append(i)
a=max(x);b=min(y)
print(a-b)
