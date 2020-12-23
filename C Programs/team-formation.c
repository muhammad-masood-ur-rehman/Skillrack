Team Formation
Team Formation: In a class, there are three types of students. C students are coders, M are mathematicians and X students have no specialization. The values of C, M and X are passed as the input to the program. The program must print the maximum number of perfect teams that can be formed from the students in the class. A perfect team includes at least one coder, at least one mathematician and it consists of exactly three members.
Boundary Condition(s):
0 <= C, M, X <= 10^9
Input Format:
The first line contains C, M and X separated by a space.
Output Format:
The first line contains the maximum number of perfect teams.
Example Input/Output 1:
Input:
4 4 1
Output:
3
Explanation:
The first team contains one coder, one mathematician and one student with no specialization. Then the remaining students in the three types are 3 3 0.
The second team contains two coders, one mathematician. Now the remaining students in the three types are 1 2 0.
The third team contains one coders, two mathematicians. Then the remaining students in the three types are 0 0 0.
Hence the output is 3
Example Input/Output 2:
Input:
1 0 2
Output:
0
#include <stdio.h>
#include <stdlib.h>

int main()
{
    long int r,n,m,i,k,c=0;
    scanf("%ld%ld%ld",&n,&m,&k);
    r=(n<=m&&n<=k)?n:(m<=n&&m<=k)?m:k;
    c+=r;
    n-=r;
    m-=r;
    k-=r;
    while((n>1||m>1)&&n>0&&m>0){
        if(n>=m){
            n-=2;
            m--;
            c++;
        }
        else if(n<=m){
            m-=2;
            n--;
            c++;
        }
    }
    printf("%ld",c);
}
