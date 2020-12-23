DP - Longest Common Substring Length
Two string values S1 and S2 are passed as the input to the program. The program must print the length of the longest common substring.
Boundary Condition(s):
1 <= Length of S1, S2 <= 10^4
Input Format:
The first line contains the value of S1.
The second line contains the value of S2.
Output Format:
The first line contains the integer value denoting the length of the longest common substring.
Example Input/Output 1:
Input:
abcde
cdefg
Output:
3
Explanation:
cde is the longest common substring whose length is 3.
def fun(x,y,m,n):
    l=[[0 for k in range(n+1)] for l in range(m+1)]
    res=0 
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                l[i][j]=0
            elif(x[i-1]==y[j-1]):
                l[i][j]=l[i-1][j-1]+1 
                res=max(res,l[i][j])
            else:
                l[i][j]=0 
    return res 
x=input().strip()
y=input().strip()
m,n=len(x),len(y)
print(fun(x,y,m,n))
