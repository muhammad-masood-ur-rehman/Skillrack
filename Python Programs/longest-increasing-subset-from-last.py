Longest Increasing Subset - From Last
Longest Increasing Subset - From Last: Given N numbers, the program must print the longest increasing subset from the end. If multiple subsets are present with the same longest length print the first occurring subset.
Input Format:
The first line contains N.
The second line contains N numbers separated by space.
Output Format:
The first line contains the longest increasing subset.
Boundary Conditions:
2 <= N <= 9999
Value of a given number is from -99999 to 99999
Example Input/Output 1:
Input:
8
2 18 18 11 6 17 11 4
Output:
4 11 17
Explanation:
There are two subsets which are of increasing values and of length 3 from the end - 4 11 17 and 6 11 18.
As 4 11 17 appears first (from the end) it is printed as the output.
n=int(input())
p=[]
l=list(map(int,input().split()))[::-1]
r=[l[i:j] for i in range(n) for j in range(i,n+1)]
for i in r:
    if len(i)==1:
        p.append(i)
    else:
        x=0
        for j in range(len(i)-1):
            if i[j]>=i[j+1]:
              x=1
        if x==0 and i!=[]:
            p.append(i)
k=max(p,key=len)
for i in k:
    print(i,end=' ')
