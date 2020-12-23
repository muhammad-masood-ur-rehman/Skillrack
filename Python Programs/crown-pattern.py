Crown Pattern
The program must accept an odd integer N as the input. The program must print a grid of characters representing the crown pattern based on the following conditions.
- The number of rows R in the grid must be (N-1)/2.
- The number of columns C in the grid must be N.
- In the 1st row of the grid, the first column, the middle column and the last column have the asterisks (*). The remaining columns in the 1st row have the plus symbols (+).
- In the 2nd row of the grid, the first column, the middle column and the last column have the hash symbols (#). The remaining columns in the 2nd row have the plus symbols (+).
- In the 3rd row of the grid, the first 2 columns, the middle 3 columns and the last 2 columns have the hash symbols (#). The remaining columns in the 3rd row have the plus symbols (+).
- In the 4th row of the grid, the first 3 columns, the middle 5 columns and the last 3 columns have the hash symbols (#). The remaining columns in the 4th row have the plus symbols (+).
- Similarly, the first R - ((R-1)/2) lines of the grid (consider the integer division for / operation).
- The remaining rows of the grid have only hash symbols (#).
Finally, the program must print the RxC grid as the output.
Boundary Condition(s):
7 <= N <= 99
Input Format:
The first line contains N.
Output Format:
The first R lines, each contains C characters based on the given conditions.
Example Input/Output 1:
Input:
11
Output:
*++++*++++*
#++++#++++#
##++###++##
###########
###########
Explanation:
Here N = 11.
The number of rows in the grid = (11-1)/2 = 5.
The number of rows in the grid = 11.
So the grid of size 5x11 is formed as given below.
*++++*++++*
#++++#++++#
##++###++##
###########
###########
Example Input/Output 2:
Input:
9
Output:
*+++*+++*
#+++#+++#
##+###+##
#########
Example Input/Output 3:
Input:
17
Output:
*+++++++*+++++++*
#+++++++#+++++++#
##+++++###+++++##
###+++#####+++###
####+#######+####
#################
#################
#################
n=int(input());s=0
r=(n-1)//2
ml=n//2;mr=n//2
e=n-1
f=(n-3)//2
print('*'+'+'*f+'*'+'+'*f+'*')
for i in range(1,r):
    s+=1 
    e-=1 
    ml-=1;mr+=1 
    for j in range(0,n):
        if(j<s or j>e) or(j>ml and j<mr):
            print('#',end="")
        else:
            print("+",end="")
    print()
