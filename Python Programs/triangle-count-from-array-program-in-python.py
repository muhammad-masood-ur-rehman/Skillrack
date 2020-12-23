Triangle Count from Array Program In Python
An array of N integers is passed as the input to the program. The program must print the count of triangles that can be formed with the given integer values. 
Note: Sum of any two sides in a triangle must be greater than the third side.
Boundary Condition(s):
3 <= N <= 500
1 <= Value of each integer <= 10000
Input Format:
The first line contains N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains the count of triangles formed from the array.
Example Input/Output 1:
Input:
5
2 1 5 4 3
Output:
3
Explanation:
The triangles formed are:
2 3 4
2 4 5
3 4 5
Example Input/Output 2:
Input:
7
7 5 2 2 9 3 10
Output:
10
Python Program for Triangle Count from Array:
def TriCount(lis,n):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(lis[i]+lis[j]>lis[k] and lis[i]+lis[k]>lis[j] and lis[k]+lis[j]>lis[i]):
                    c+=1 
    return c 
n=int(input())
lis=list(map(int,input().split()))
length=len(lis)
print(TriCount(lis,length))
