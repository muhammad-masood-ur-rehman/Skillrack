DP - Maximum Sum Subarray
An array of N integers (both positive and negative) is given as the input to the program. The program must print the maximum sum of the subarray in the given array as the output.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains N.
The second line contains N integers separated by space.
Output Format:
The first line contains the maximum subarray sum.
Example Input/Output 1:
Input:
7
2 1 -6 4 -2 8 -2
Output:
10
Explanation:
The subarray 4 -2 8 has the maximum sum 10.
Example Input/Output 2:
Input:
10
73 64 18 -18 44 -4 -17 -28 -59 54
Output:
181
def func(a,size):
    m=a[0]
    cm=a[0]
    for i in range(1,size):
        cm=max(a[i],cm+a[i])
        m=max(m,cm)
    return m 
n=int(input())
a=list(map(int,input().split()))
print(func(a,len(a)))
