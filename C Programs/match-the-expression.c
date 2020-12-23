Match the Expression
Series of N expression(including serial number) and values are given as input, the program must match the values to the expression by printing the serial number of value for each expression. The allowed operations are addition, subtraction, multiplication, division and modulo(remainder).
Boundary Condition(s):
2 <= N <= 100
Input Format:
The first line contains the value of N.
The next N lines contain expression(including serial number) and value separated by space(s).
Output Format:
The first line contains the serial number of value for each expression separated by space.
Example Input/Output1:
Input:
3
1.1+2+3 2
2.1*5-4 6
3.3%3+2 1
Output:
2 3 1
Explanation:
1+2+3 value is 6. 6 is matched to the expression at serial number 2.
1*5-4 value is 1. 1 is matched to the expression at serial number 3.
3%3+2 value is 2. 2 is matched to the expression at serial number 1.
So the output is 2 3 1.
Example Input/Output2:
Input:
4
1.255%10 100
2.11*2-2 50
3.99*1+1 20
4.76/2+12 5
Output:
4 3 1 2
#include<stdio.h>
#include <stdlib.h>

int main(){
    int num,bar,tn;
    char foo,tc;
    scanf("%d",&num);
    int stri,ans[num],matrix1[num];
    for(int ele=0;ele<num;ele++){
        scanf("%d. ",&stri);
        scanf("%d%c",&tn,&tc);
        while(scanf("%d%c",&bar,&foo)==2){
            if(tc=='+')
            tn+=bar;
            else if(tc=='-')
            tn-=bar;
            else if(tc=='*')
            tn*=bar;
            else if(tc=='/')
            tn/=bar;
            else 
            tn%=bar;
            tc=foo;
            if(foo=='\r'||foo==' '||foo=='\n')
            break;
        }
        ans[ele]=tn;
        scanf("%d",&matrix1[ele]);
    }
    for(int ele=0;ele<num;ele++){
        for(int j=0;j<num;j++){
            if(ans[ele]==matrix1[j]){
                printf("%d ",j+1);
                break;
            }
        }
    }
}
Tehd
