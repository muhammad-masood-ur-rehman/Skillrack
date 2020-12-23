Check Sorted Order
The program must accept N integers which are sorted in ascending order except one integer. But if that single integer R is reversed, the entire array will be in sorted order. The program must print the first integer that must be reversed so that the entire array will be sorted in ascending order.
Boundary Condition(s):
2 <= N <= 20
Input Format:
The first line contains N.
The second line contains N integer values separated by a space.
Output Format:
The first line contains the integer value R.
Example Input/Output 1:
Input:
5
10 71 20 30 33
Output:
71
Explanation:
When 71 is reversed the array becomes sorted as below.
10 17 20 30 33
Example Input/Output 2:
Input:
6
10 20 30 33 64 58
Output:
64
Example Input/Output 3:
Input:
6
10 20 30 33 67 58
Output:
58
def rev(n):
    reve=0  
    while(n>0):
        r=n%10
        reve=reve*10+r  
        n=n//10 
    return reve 
n=int(input())
l=list(map(int,input().split()));ind=0
while(True):
    number=l[ind]
    r=rev(number)
    l[ind]=r  
    if l==sorted(l):
        print(number)
        break
    else:
        l[ind]=number 
    ind+=1
