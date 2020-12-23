Longest Common Subsequence Length
The program must accept two string values A and B as the input. The program must print the length of the longest common subsequence of the two string values as the output. A common subsequence is a group of characters present in both the string values in the same order.
Boundary Condition(s):
1 <= A, B <= 1000
Input Format:
The first line contains A.
The second line contains B.
Output Format:
The first line contains the longest common subsequence of A and B.
Example Input/Output 1:
Input:
britanica
rtiac
Output:
4
Explanation:
The common subsequence of the two string values are riac.
Example Input/Output 2:
Input:
smartphone
marketplace
Output:
6
def lcsl(x,y):
    m=len(x)
    n=len(y)
    l=[[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1 
            else:
                l[i][j]=max(l[i-1][j], l[i][j-1])
    return l[m][n]
x=input().strip()
y=input().strip()
print(lcsl(x,y))
