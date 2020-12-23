Square Free Numbers - TCS CodeVita
The program must accept an integer N as the input. The program must print the number of square free numbers that divide the given integer N as the output.
A square free number is one that is not divisible by a perfect square (other than 1). Note that 1 is not considered a square free number.
Boundary Condition(s):
1 <= N < 10^9
Input Format:
The first line contains N.
Output Format:
The first line contains an integer representing the number of square free numbers that divide the given integer N.
Example Input/Output 1:
Input:
20
Output:
3
Explanation:
Here N = 20.
The integers that divide 20 are given below.
1, 2, 4, 5, 10, 20
1 is not a square free number.
4 is a perfect square.
20 is divisible by 4, which is a perfect square.
2 and 5 are prime numbers. So they are square free numbers.
10 is divisible by 1, 2, 5 and 10, and none of them are perfect squares.
Hence the square free numbers that divide 20 are 2, 5 and 10.
Hence the output is 3
Example Input/Output 2:
Input:
72
Output:
3
Explanation:
Here N = 72.
The integers that divide 72 are given below.
1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72
1 is not a square free number.
4, 9 and 36 are perfect squares.
8, 12, 18, 24 and 72 are divisible by one of the perfect squares.
Hence only 2, 3 and 6 are square free. (It is easily seen that none of them are divisible by a perfect square).
Hence the output is 3
C:
#include <stdio.h>
#include <math.h>
int main()
{
    long int n;
    double sqnum;
    long int i,j=0,flag,chksqr,temp[10000];
    int count=0,k;
    scanf("%ld",&n);
    
    for(i=2;i<=n/2;i++)
    {
        if(n%i==0)
        {    
            count++;
            sqnum=sqrt(i);
            chksqr=sqnum;
            if(chksqr==sqnum)
            {
                count--;
                temp[j]=i;
                j++;
            }
            else
            {
                for(k=0;k<j;k++) { if(i>temp[k] && j!=0)
                    {
                        if(i%temp[k]==0)
                        {	
                          	count--;
                        	k=j+1;
                        }
                    }
                    else
                        break;
                }
            }
        }
    }

    printf("%d",count);
    return 0;
}
Python:
from math import sqrt
def isSquareFree(n):
    if n % 2 == 0:
        n = n / 2
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1)):
        if n % i == 0:
            n = n / i
        if n % i == 0:
            return False
    return True
num=int(input())
squarefree=[]
fac = []
for i in range(1, num + 1):
    if num % i == 0:
        fac.append(i)
for i in fac[1:]:
    if isSquareFree(i):
        squarefree.append(i)
print(len(squarefree))
