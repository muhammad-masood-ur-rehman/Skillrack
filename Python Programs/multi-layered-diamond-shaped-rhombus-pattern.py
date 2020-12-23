Multi Layered Diamond Shaped Rhombus Pattern
Given an odd value of N, the program must print multi layered rhombus pattern in diamond shapes whose side contains N, N-2, ... 1 slashes respectively as shown below in the examples.Input Format:
The first line contains N.
Output Format:
The multi layered rhombus pattern in diamond shapes whose side contains N, N-2, ... 1 slashes respectively. Hash symbol is used as filler for other values.
Boundary Conditions:
1 <= N <= 101 and N is odd.
Example Input/Output:
Input:
5
Output:
####/\####
###/##\###
##/#/\#\##
#/#/##\#\#
/#/#/\#\#\
\#\#\/#/#/
#\#\##/#/#
##\#\/#/##
###\##/###
####\/####
n = int(input())
for i in range(2*n):
    for j in range(2*n):
        if i<n and j<n and j>=n-i-1 and (j-n+1+i)%2==0:
            print('/',end='')
        elif i<n and j>=n and j<=n+i and (j-n-i)%2==0:
            print('\\',end='')
        elif i>=n and j<n and j>=i-n and (j-i+n)%2==0:
            print('\\',end='')
        elif i>=n and j>=n and j<=3*n-i-1 and (3*n-i-1-j)%2==0:
            print('/',end='')
        else:
            print('#',end='')
    print()  
