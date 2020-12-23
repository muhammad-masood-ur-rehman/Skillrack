Positive Even Integers
The program must accept N integers and print the first K positive even integers as the output.
Note:
- At least K positive even integers are always present in the given N integers.
- 0 is neither positive nor negative.
Boundary Condition(s):
1 <= K <= N <= 100
-10^5 <= Each integer value <= 10^5
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.
Output Format:
The first line contains the first K positive even integers separated by a space.
Example Input/Output 1:
Input:
10
-84 36 23 8 -25 0 14 -78 42 20
4
Output:
36 8 14 42
Explanation:
Here N = 10 and K = 4.
The given 10 integers are -84, 36, 23, 8, -25, 0, 14, -78, 42 and 20.
The first 4 positive even integers are 36, 8, 14 and 42.
Hence the output is
36 8 14 42
Example Input/Output 2:
Input:
8
-4 -5 44 -29 -9 2 11 26
3
Output:
44 2 26
num=int(input())
List1=list(map(int,input().split()))
tofind=int(input())
List2=[]
for ele in List1:
    if ele>0:
        if ele%2==0:
            List2.append(ele)
print(*List2[:tofind])
