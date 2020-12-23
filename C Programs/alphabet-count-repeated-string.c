Alphabet Count - Repeated String
A string S is passed as input to the program. The string S is repeated till the repeated string R is of length N. The program must print the count of a specific alphabet A which is passed as the input in the repeated string R.
Input Format:
The first line contains S.
The second line contains N.
The third line contains A.
Output Format:
The first line contains the count of the alphabet A in the repeated string R.
Boundary Conditions:
1 <= Length of S <= 50
1 <= N <= 9999999
A is from a to z
Example Input/Output 1:
Input:
abcd
10
b
Output:
3
Explanation:
abcd when repeated till length 10 is abcdabcdab in which the alphabet b occurs 3 times.
S = input().strip()
N = int(input())
A = input().strip()
count = 0
 
while len(S) <= N:
    S+=S
for i in range(N):
    if(S[i] == A):
        count += 1
print(count)
#include<stdio.h>
#include <stdlib.h>
 
int main()
{
    char s[99999];
    int n,i=0,j=0,c=0,flag=0;
    char a;
    scanf("%s %d %c",s,&n,&a);
    while(j!=n)
    {
        for(i=0;i<strlen(s);i++)
        {
            if(s[i]==a)
            {
                c++;
            }
            j++;
            if(j==n)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
        {
            break;
        }
    }
    printf("%d",c);
}
