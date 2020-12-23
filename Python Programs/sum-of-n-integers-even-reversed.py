Sum of N Integers - Even Reversed
The program must accept N integers and print the sum S of all POSITIVE integers with the even positive integers reversed.
Input Format:
The first line will contain N.
The second line will contain N integers separated by a space.
Output Format:
The first line will contain S.
Boundary Conditions:
1 <= N <= 100000
Example Input/Output 1:
Input:
4
39 -8 57 24
Output:
138
Explanation:
The sum = 39+57+42 = 138 (The even number 24 is reversed)
Example Input/Output 2:
Input:
3
-23 -11 -445
Output:
0
n=int(input());k=[]
l=list(map(str,input().split()))
for i in l:
    if int(i)>0:
        if int(i)%2==0:k.append(int(i[::-1]))
        else:k.append(int(i))
print(sum(k))
